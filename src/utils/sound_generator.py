# 音效生成工具
# 负责为剧本添加音效标注

class SoundGenerator:
    """
    音效生成类
    
    负责为剧本添加音效标注，确保音效标注符合规范
    """
    
    def __init__(self):
        """
        初始化音效生成器
        """
        pass
    
    def generate_sound(self, sound, description=None):
        """
        生成音效标注
        
        Args:
            sound (str): 音效描述
            description (str, optional): 音效来源说明
            
        Returns:
            str: 音效标注文本
        """
        if description:
            return f"声音提示：{sound}（{description}）\n"
        else:
            return f"声音提示：{sound}\n"
    
    def generate_combat_sound(self, action):
        """
        生成战斗音效
        
        Args:
            action (str): 战斗动作
            
        Returns:
            str: 战斗音效标注
        """
        sound_map = {
            "挥刀": "唰",
            "拔剑": "锵",
            "砍中": "当",
            "踢中": "砰",
            "骨折": "咔嚓",
            "吐血": "噗",
            "爆炸": "BOOM"
        }
        
        sound = sound_map.get(action, "啪")
        return self.generate_sound(sound, f"{action}声")
    
    def generate_environment_sound(self, environment):
        """
        生成环境音效
        
        Args:
            environment (str): 环境描述
            
        Returns:
            str: 环境音效标注
        """
        sound_map = {
            "开门": "吱呀",
            "关门": "砰",
            "脚步声": "踏踏",
            "风声": "呼呼",
            "雨声": "滴答",
            "雷声": "轰隆",
            "鸟鸣": "啾啾"
        }
        
        sound = sound_map.get(environment, "")
        if sound:
            return self.generate_sound(sound, f"{environment}声")
        else:
            return ""
