# 剧本生成器核心类
# 负责协调各个生成器的工作，生成符合要求的剧本

import os
from utils.config_manager import ConfigManager
from data.data_manager import DataManager


class ScriptGenerator:
    """
    剧本生成器核心类
    
    负责协调各个生成器的工作，生成符合要求的剧本
    """
    
    def __init__(self, config_manager=None, data_manager=None):
        """
        初始化剧本生成器
        
        Args:
            config_manager (ConfigManager): 配置管理器
            data_manager (DataManager): 数据管理器
        """
        self.config_manager = config_manager or ConfigManager()
        self.data_manager = data_manager or DataManager()
        self.output_dir = self.config_manager.get_output_dir()
        
        os.makedirs(self.output_dir, exist_ok=True)
    
    def generate_script(self, episode):
        """
        生成指定集数的剧本
        
        Args:
            episode (int): 集数
            
        Returns:
            str: 生成的剧本内容
        """
        outline = self.data_manager.get_outline(episode)
        
        if episode == 1:
            from generator.first_episode import FirstEpisodeGenerator
            generator = FirstEpisodeGenerator(self.config_manager, self.data_manager)
        elif episode == 2:
            from generator.second_episode import SecondEpisodeGenerator
            generator = SecondEpisodeGenerator(self.config_manager, self.data_manager)
        else:
            from generator.smart_episode_generator import SmartEpisodeGenerator
            generator = SmartEpisodeGenerator(self.config_manager, self.data_manager)
        
        script_content = generator.generate(episode, outline)
        
        self.save_script(episode, script_content)
        
        return script_content
    
    def generate_all_scripts(self, start_episode=1, end_episode=70):
        """
        生成所有集数的剧本
        
        Args:
            start_episode (int): 开始集数
            end_episode (int): 结束集数
            
        Returns:
            dict: 生成的剧本字典，键为集数，值为剧本内容
        """
        scripts = {}
        
        for episode in range(start_episode, end_episode + 1):
            print(f"生成第{episode}集剧本...")
            script_content = self.generate_script(episode)
            scripts[episode] = script_content
            print(f"第{episode}集剧本生成完成")
        
        return scripts
    
    def save_script(self, episode, content):
        """
        保存剧本到文件
        
        Args:
            episode (int): 集数
            content (str): 剧本内容
        """
        file_path = os.path.join(self.output_dir, f"第{episode}集.md")
        
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"剧本已保存到: {file_path}")
        except Exception as e:
            print(f"保存剧本失败: {e}")
    
    def load_script(self, episode):
        """
        加载已生成的剧本
        
        Args:
            episode (int): 集数
            
        Returns:
            str: 剧本内容或空字符串
        """
        file_path = os.path.join(self.output_dir, f"第{episode}集.md")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            return content
        except Exception as e:
            print(f"加载剧本失败: {e}")
            return ""
    
    def validate_script(self, episode):
        """
        验证剧本
        
        Args:
            episode (int): 集数
            
        Returns:
            list: 验证问题列表
        """
        from generator.consistency_validator import ConsistencyValidator
        from generator.state_tracker import StateTracker
        
        state_tracker = StateTracker(self.data_manager)
        validator = ConsistencyValidator(state_tracker)
        
        content = self.load_script(episode)
        if not content:
            return ["无法加载剧本内容"]
        
        result = validator.validate(episode, content)
        return result.get("issues", [])
