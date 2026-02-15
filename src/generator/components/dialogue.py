# 对话组件
# 负责生成对话和OS


class DialogueComponent:
    """
    对话组件
    
    负责生成对话和OS
    """
    
    def __init__(self):
        """
        初始化对话组件
        """
        pass
    
    def generate(self, character_name, dialogue, action=None):
        """
        生成对话
        
        Args:
            character_name (str): 人物名称
            dialogue (str): 对话内容
            action (str): 动作/表情
            
        Returns:
            str: 对话内容
        """
        if action:
            return f"{character_name}（{action}）：{dialogue}\n"
        else:
            return f"{character_name}：{dialogue}\n"
    
    def generate_os(self, character_name, os_content):
        """
        生成OS（内心独白）
        
        Args:
            character_name (str): 人物名称
            os_content (str): OS内容
            
        Returns:
            str: OS内容
        """
        return f"{character_name}（OS）：{os_content}\n"
    
    def generate_narrator(self, content):
        """
        生成旁白
        
        Args:
            content (str): 旁白内容
            
        Returns:
            str: 旁白内容
        """
        return f"旁白：{content}\n"
    
    def generate_system(self, content):
        """
        生成系统提示
        
        Args:
            content (str): 系统提示内容
            
        Returns:
            str: 系统提示内容
        """
        return f"系统：{content}\n"
    
    def generate_sound(self, sound_type, description):
        """
        生成声音提示
        
        Args:
            sound_type (str): 声音类型
            description (str): 描述
            
        Returns:
            str: 声音提示
        """
        return f"声音提示：{sound_type}（{description}）\n"
