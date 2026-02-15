# 场景选择工具
# 负责根据剧情需要选择合适的场景

class SceneSelector:
    """
    场景选择类
    
    负责根据剧情需要选择合适的场景，确保场景描述一致
    """
    
    def __init__(self, data_manager):
        """
        初始化场景选择器
        
        Args:
            data_manager (DataManager): 数据管理器
        """
        self.data_manager = data_manager
    
    def get_scene(self, scene_name):
        """
        获取指定场景信息
        
        Args:
            scene_name (str): 场景名称
            
        Returns:
            dict: 场景信息或None
        """
        scenes = self.data_manager.get_scenes()
        return scenes.get(scene_name)
    
    def select_scenes_by_category(self, category):
        """
        根据类别选择场景
        
        Args:
            category (str): 场景类别
            
        Returns:
            list: 场景列表
        """
        scenes = self.data_manager.get_scenes()
        return [scene for scene in scenes.values() if scene.get("category") == category]
    
    def select_scenes_by_time(self, time):
        """
        根据时间选择场景
        
        Args:
            time (str): 时间（如「日」、「夜」）
            
        Returns:
            list: 场景列表
        """
        scenes = self.data_manager.get_scenes()
        return [scene for scene in scenes.values() if scene.get("time") == time]
    
    def select_combat_scenes(self):
        """
        选择战斗场景
        
        Returns:
            list: 战斗场景列表
        """
        combat_categories = ["战场场景", "边关场景"]
        combat_scenes = []
        
        for category in combat_categories:
            combat_scenes.extend(self.select_scenes_by_category(category))
        
        return combat_scenes
    
    def select_royal_scenes(self):
        """
        选择皇宫场景
        
        Returns:
            list: 皇宫场景列表
        """
        return self.select_scenes_by_category("皇宫场景")
    
    def select_city_scenes(self):
        """
        选择城市场景
        
        Returns:
            list: 城市场景列表
        """
        city_categories = ["长安城场景"]
        city_scenes = []
        
        for category in city_categories:
            city_scenes.extend(self.select_scenes_by_category(category))
        
        return city_scenes
    
    def select_private_scenes(self):
        """
        选择私人场景
        
        Returns:
            list: 私人场景列表
        """
        private_categories = ["核心场景"]
        private_scenes = []
        
        for category in private_categories:
            private_scenes.extend(self.select_scenes_by_category(category))
        
        return private_scenes
