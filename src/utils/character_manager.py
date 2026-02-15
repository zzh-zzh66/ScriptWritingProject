# 角色管理工具
# 负责管理角色的出场和行为，确保人设一致

class CharacterManager:
    """
    角色管理类
    
    负责管理角色的出场和行为，确保人设一致
    """
    
    def __init__(self, data_manager):
        """
        初始化角色管理器
        
        Args:
            data_manager (DataManager): 数据管理器
        """
        self.data_manager = data_manager
    
    def get_character(self, character_name):
        """
        获取指定角色信息
        
        Args:
            character_name (str): 角色名称
            
        Returns:
            dict: 角色信息或None
        """
        return self.data_manager.get_character(character_name)
    
    def get_all_characters(self):
        """
        获取所有角色信息
        
        Returns:
            dict: 角色字典
        """
        return self.data_manager.get_characters()
    
    def get_characters_by_category(self, category):
        """
        根据类别获取角色
        
        Args:
            category (str): 角色类别（如「主角」、「核心配角」等）
            
        Returns:
            list: 角色列表
        """
        characters = self.data_manager.get_characters()
        return [character for character in characters.values() if character.get("category") == category]
    
    def get_character_stage(self, character_name, stage):
        """
        获取角色在指定阶段的信息
        
        Args:
            character_name (str): 角色名称
            stage (str): 阶段（如「前期」、「中期」、「后期」）
            
        Returns:
            dict: 角色阶段信息或None
        """
        character = self.get_character(character_name)
        if character and "stages" in character:
            return character["stages"].get(stage)
        return None
    
    def get_protagonist(self):
        """
        获取主角信息
        
        Returns:
            dict: 主角信息或None
        """
        protagonists = self.get_characters_by_category("主角")
        return protagonists[0] if protagonists else None
    
    def get_core_supporting_characters(self):
        """
        获取核心配角信息
        
        Returns:
            list: 核心配角列表
        """
        return self.get_characters_by_category("核心配角")
    
    def get_main_supporting_characters(self):
        """
        获取主要配角信息
        
        Returns:
            list: 主要配角列表
        """
        return self.get_characters_by_category("主要配角")
    
    def get_minor_supporting_characters(self):
        """
        获取次要配角信息
        
        Returns:
            list: 次要配角列表
        """
        return self.get_characters_by_category("次要配角")
    
    def get_antagonists(self):
        """
        获取反派角色信息
        
        Returns:
            list: 反派角色列表
        """
        return self.get_characters_by_category("反派势力")
    
    def validate_character_consistency(self, character_name, behavior):
        """
        验证角色行为的一致性
        
        Args:
            character_name (str): 角色名称
            behavior (str): 角色行为描述
            
        Returns:
            bool: 行为是否符合角色设定
        """
        # 这里可以添加更复杂的角色行为一致性验证逻辑
        # 目前只是返回True
        return True
