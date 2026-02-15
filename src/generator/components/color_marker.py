# 颜色标记组件
# 负责生成颜色标记的描写


class ColorMarkerComponent:
    """
    颜色标记组件
    
    负责生成颜色标记的描写
    """
    
    def __init__(self):
        """
        初始化颜色标记组件
        """
        self.colors = {
            "green": "高光场景·金手指·大爽点",
            "yellow": "冲突·矛盾·纷争触发",
            "blue": "铺垫·钩子·悬念"
        }
    
    def mark(self, content, color="yellow"):
        """
        添加颜色标记
        
        Args:
            content (str): 内容
            color (str): 颜色（green/yellow/blue）
            
        Returns:
            str: 带颜色标记的内容
        """
        return f"【{color.upper()}】{content}"
    
    def mark_green(self, content):
        """
        添加绿色标记（高光场景）
        
        Args:
            content (str): 内容
            
        Returns:
            str: 带绿色标记的内容
        """
        return self.mark(content, "green")
    
    def mark_yellow(self, content):
        """
        添加黄色标记（冲突场景）
        
        Args:
            content (str): 内容
            
        Returns:
            str: 带黄色标记的内容
        """
        return self.mark(content, "yellow")
    
    def mark_blue(self, content):
        """
        添加蓝色标记（钩子场景）
        
        Args:
            content (str): 内容
            
        Returns:
            str: 带蓝色标记的内容
        """
        return self.mark(content, "blue")
    
    def generate_highlight_scene(self, description, color="green"):
        """
        生成高光场景
        
        Args:
            description (str): 场景描述
            color (str): 颜色
            
        Returns:
            str: 高光场景内容
        """
        return f"【{color.upper()}】△{description}。\n"
