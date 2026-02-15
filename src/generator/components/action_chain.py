# 动作链组件
# 负责拆分和生成动作描写


class ActionChainComponent:
    """
    动作链组件
    
    负责拆分和生成动作描写
    """
    
    def __init__(self):
        """
        初始化动作链组件
        """
        self.max_length = 50
    
    def generate(self, action):
        """
        生成单个动作描写
        
        Args:
            action (str): 动作描写
            
        Returns:
            str: 动作描写
        """
        return f"△{action}。\n"
    
    def generate_chain(self, actions):
        """
        生成动作链
        
        Args:
            actions (list): 动作列表
            
        Returns:
            str: 动作链内容
        """
        content = ""
        for action in actions:
            content += self.generate(action)
        return content
    
    def split_long_action(self, action):
        """
        拆分过长的动作描写
        
        Args:
            action (str): 原始动作描写
            
        Returns:
            list: 拆分后的动作列表
        """
        if len(action) <= self.max_length:
            return [action]
        
        actions = []
        
        connectors = ['，', '。', '；']
        parts = []
        current = ""
        
        for char in action:
            current += char
            if char in connectors and len(current) >= 20:
                parts.append(current.strip('，。；'))
                current = ""
        
        if current:
            parts.append(current.strip('，。；'))
        
        for part in parts:
            if part and len(part) > 0:
                actions.append(part)
        
        return actions if actions else [action]
    
    def generate_with_color(self, action, color="yellow"):
        """
        生成带颜色标记的动作描写
        
        Args:
            action (str): 动作描写
            color (str): 颜色（yellow/green/blue）
            
        Returns:
            str: 带颜色标记的动作描写
        """
        return f"【{color.upper()}】△{action}。\n"
    
    def generate_combat_action(self, attacker, action, target=None, result=None):
        """
        生成战斗动作
        
        Args:
            attacker (str): 攻击者
            action (str): 动作
            target (str): 目标
            result (str): 结果
            
        Returns:
            str: 战斗动作内容
        """
        content = ""
        
        if target:
            content += f"△{attacker}{action}{target}。\n"
        else:
            content += f"△{attacker}{action}。\n"
        
        if result:
            content += f"△{result}。\n"
        
        return content
