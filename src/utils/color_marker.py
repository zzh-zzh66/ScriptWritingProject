# 颜色标记工具
# 负责为剧本添加颜色标记

class ColorMarker:
    """
    颜色标记类
    
    负责为剧本添加颜色标记，包括绿色（高光场景）、黄色（冲突场景）和蓝色（钩子场景）
    """
    
    def __init__(self):
        """
        初始化颜色标记器
        """
        pass
    
    def mark_green(self, text):
        """
        标记绿色（高光场景·金手指·大爽点）
        
        Args:
            text (str): 需要标记的文本
            
        Returns:
            str: 标记后的文本
        """
        return f"【绿色】{text}"
    
    def mark_yellow(self, text):
        """
        标记黄色（冲突·矛盾·纷争触发）
        
        Args:
            text (str): 需要标记的文本
            
        Returns:
            str: 标记后的文本
        """
        return f"【黄色】{text}"
    
    def mark_blue(self, text):
        """
        标记蓝色（铺垫·钩子·悬念）
        
        Args:
            text (str): 需要标记的文本
            
        Returns:
            str: 标记后的文本
        """
        return f"【蓝色】{text}"
