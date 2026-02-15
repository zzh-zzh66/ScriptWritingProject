# 人物出场组件
# 负责生成人物出场描写（外貌描写+悬浮字介绍）


class CharacterIntroComponent:
    """
    人物出场组件
    
    负责生成人物出场描写（外貌描写+悬浮字介绍）
    """
    
    def __init__(self, state_tracker):
        """
        初始化人物出场组件
        
        Args:
            state_tracker (StateTracker): 状态跟踪器
        """
        self.state_tracker = state_tracker
    
    def generate(self, character_name, episode, custom_appearance=None, custom_description=None):
        """
        生成人物出场
        
        Args:
            character_name (str): 人物名称
            episode (int): 集数
            custom_appearance (str): 自定义外貌描写
            custom_description (str): 自定义身份描述
            
        Returns:
            str: 人物出场内容
        """
        content = ""
        
        appearance = custom_appearance or self.state_tracker.get_character_appearance(character_name, episode)
        identity = custom_description or self.state_tracker.get_character_identity(character_name, episode)
        
        if appearance:
            content += f"△{appearance}\n"
        
        if identity:
            content += f"△金色字体，竖向，悬浮在{character_name}旁边，显示：{character_name}：{identity}\n"
        
        return content
    
    def generate_with_action(self, character_name, episode, action, custom_appearance=None, custom_description=None):
        """
        生成带动作的人物出场
        
        Args:
            character_name (str): 人物名称
            episode (int): 集数
            action (str): 动作描写
            custom_appearance (str): 自定义外貌描写
            custom_description (str): 自定义身份描述
            
        Returns:
            str: 人物出场内容
        """
        content = ""
        
        appearance = custom_appearance or self.state_tracker.get_character_appearance(character_name, episode)
        identity = custom_description or self.state_tracker.get_character_identity(character_name, episode)
        
        if appearance and action:
            content += f"△{character_name}{action}，{appearance}\n"
        elif appearance:
            content += f"△{appearance}\n"
        elif action:
            content += f"△{character_name}{action}。\n"
        
        if identity:
            content += f"△金色字体，竖向，悬浮在{character_name}旁边，显示：{character_name}：{identity}\n"
        
        return content
    
    def generate_simple(self, character_name, description):
        """
        生成简单人物介绍
        
        Args:
            character_name (str): 人物名称
            description (str): 身份描述
            
        Returns:
            str: 人物介绍内容
        """
        return f"△金色字体，竖向，悬浮在{character_name}旁边，显示：{character_name}：{description}\n"
