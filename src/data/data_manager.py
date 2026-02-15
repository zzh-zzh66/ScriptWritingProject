# 数据管理模块
# 负责管理解析后的数据，提供数据访问接口，确保数据一致性

class DataManager:
    """
    数据管理类
    
    负责管理解析后的数据，包括：
    - 存储解析后的数据
    - 提供数据访问接口
    - 确保数据一致性
    """
    
    def __init__(self):
        """
        初始化数据管理器
        """
        self.data = {
            "characters": {},  # 人物数据
            "scenes": {},      # 场景数据
            "outlines": {},    # 剧情大纲数据
            "settings": {},    # 设定数据
            "episodes": {}     # 剧集数据
        }
    
    def set_characters(self, characters):
        """
        设置人物数据
        
        Args:
            characters (dict): 人物数据
        """
        self.data["characters"] = characters
    
    def get_characters(self):
        """
        获取人物数据
        
        Returns:
            dict: 人物数据
        """
        return self.data["characters"]
    
    def get_character(self, name):
        """
        获取指定人物数据
        
        Args:
            name (str): 人物名称
            
        Returns:
            dict: 人物数据或None
        """
        return self.data["characters"].get(name)
    
    def set_scenes(self, scenes):
        """
        设置场景数据
        
        Args:
            scenes (dict): 场景数据
        """
        self.data["scenes"] = scenes
    
    def get_scenes(self):
        """
        获取场景数据
        
        Returns:
            dict: 场景数据
        """
        return self.data["scenes"]
    
    def get_scene(self, name):
        """
        获取指定场景数据
        
        Args:
            name (str): 场景名称
            
        Returns:
            dict: 场景数据或None
        """
        return self.data["scenes"].get(name)
    
    def set_outlines(self, outlines):
        """
        设置剧情大纲数据
        
        Args:
            outlines (dict): 剧情大纲数据
        """
        self.data["outlines"] = outlines
    
    def get_outlines(self):
        """
        获取剧情大纲数据
        
        Returns:
            dict: 剧情大纲数据
        """
        return self.data["outlines"]
    
    def get_outline(self, episode):
        """
        获取指定集数的剧情大纲
        
        Args:
            episode (int): 集数
            
        Returns:
            dict: 剧情大纲数据或None
        """
        return self.data["outlines"].get(episode)
    
    def set_settings(self, settings):
        """
        设置设定数据
        
        Args:
            settings (dict): 设定数据
        """
        self.data["settings"] = settings
    
    def get_settings(self):
        """
        获取设定数据
        
        Returns:
            dict: 设定数据
        """
        return self.data["settings"]
    
    def get_setting(self, key):
        """
        获取指定设定数据
        
        Args:
            key (str): 设定键
            
        Returns:
            设定值或None
        """
        return self.data["settings"].get(key)
    
    def set_episode(self, episode, data):
        """
        设置剧集数据
        
        Args:
            episode (int): 集数
            data (dict): 剧集数据
        """
        self.data["episodes"][episode] = data
    
    def get_episode(self, episode):
        """
        获取指定剧集数据
        
        Args:
            episode (int): 集数
            
        Returns:
            dict: 剧集数据或None
        """
        return self.data["episodes"].get(episode)
    
    def get_all_episodes(self):
        """
        获取所有剧集数据
        
        Returns:
            dict: 所有剧集数据
        """
        return self.data["episodes"]
    
    def clear(self):
        """
        清空所有数据
        """
        self.data = {
            "characters": {},
            "scenes": {},
            "outlines": {},
            "settings": {},
            "episodes": {}
        }
    
    def validate_consistency(self):
        """
        验证数据一致性
        
        Returns:
            list: 一致性问题列表
        """
        issues = []
        
        # 验证人物数据一致性
        if not self.data["characters"]:
            issues.append("人物数据为空")
        
        # 验证场景数据一致性
        if not self.data["scenes"]:
            issues.append("场景数据为空")
        
        # 验证剧情大纲数据一致性
        if not self.data["outlines"]:
            issues.append("剧情大纲数据为空")
        
        # 验证设定数据一致性
        if not self.data["settings"]:
            issues.append("设定数据为空")
        
        return issues
