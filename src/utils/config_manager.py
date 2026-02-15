# 配置管理工具
# 负责加载和管理配置文件

import yaml
import os

class ConfigManager:
    """
    配置管理类
    
    负责加载和管理配置文件，提供配置访问接口
    """
    
    def __init__(self, config_path="config/config.yaml"):
        """
        初始化配置管理器
        
        Args:
            config_path (str): 配置文件路径
        """
        self.config_path = config_path
        self.config = self.load_config()
    
    def load_config(self):
        """
        加载配置文件
        
        Returns:
            dict: 配置数据
        """
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
            return config
        except Exception as e:
            print(f"加载配置文件失败: {e}")
            return {}
    
    def get(self, key, default=None):
        """
        获取配置值
        
        Args:
            key (str): 配置键，支持嵌套键，如 "project.name"
            default: 默认值
            
        Returns:
            配置值或默认值
        """
        keys = key.split('.')
        value = self.config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def get_project_name(self):
        """
        获取项目名称
        
        Returns:
            str: 项目名称
        """
        return self.get("project.name", "AI漫剧剧本生成器")
    
    def get_project_version(self):
        """
        获取项目版本
        
        Returns:
            str: 项目版本
        """
        return self.get("project.version", "1.0.0")
    
    def get_doc_dir(self):
        """
        获取文档目录
        
        Returns:
            str: 文档目录
        """
        return self.get("paths.doc_dir", "doc")
    
    def get_outline_dir(self):
        """
        获取剧情大纲目录
        
        Returns:
            str: 剧情大纲目录
        """
        return self.get("paths.outline_dir", "doc/剧情大纲")
    
    def get_output_dir(self):
        """
        获取输出目录
        
        Returns:
            str: 输出目录
        """
        return self.get("paths.output_dir", "doc/剧本正文")
    
    def get_creativity_level(self):
        """
        获取创造性级别
        
        Returns:
            float: 创造性级别
        """
        return self.get("generation.creativity_level", 0.3)
    
    def is_first_episode_priority(self):
        """
        是否优先处理第一集
        
        Returns:
            bool: 是否优先处理第一集
        """
        return self.get("generation.first_episode_priority", True)
    
    def is_second_episode_priority(self):
        """
        是否优先处理第二集
        
        Returns:
            bool: 是否优先处理第二集
        """
        return self.get("generation.second_episode_priority", True)
    
    def is_rule_check_enabled(self):
        """
        是否启用规则检查
        
        Returns:
            bool: 是否启用规则检查
        """
        return self.get("validation.enable_rule_check", True)
    
    def is_consistency_check_enabled(self):
        """
        是否启用一致性检查
        
        Returns:
            bool: 是否启用一致性检查
        """
        return self.get("validation.enable_consistency_check", True)
    
    def is_format_check_enabled(self):
        """
        是否启用格式检查
        
        Returns:
            bool: 是否启用格式检查
        """
        return self.get("validation.enable_format_check", True)
    
    def get_logging_level(self):
        """
        获取日志级别
        
        Returns:
            str: 日志级别
        """
        return self.get("logging.level", "INFO")
    
    def get_logging_format(self):
        """
        获取日志格式
        
        Returns:
            str: 日志格式
        """
        return self.get("logging.format", "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
