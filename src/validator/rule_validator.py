# 规则验证器
# 负责验证剧本是否符合写作指南中的规则

class RuleValidator:
    """
    规则验证器
    
    负责验证剧本是否符合写作指南中的规则，包括禁止事项检查等
    """
    
    def __init__(self):
        """
        初始化规则验证器
        """
        # 禁止的表达式列表
        self.forbidden_patterns = {
            "眼神描写": [
                "眼神冷", "眼神锐利", "眼神一冷", "眼神扫过", "眼神没离开", 
                "眼神坚定", "眼神警惕", "眼神如刀", "眼神如炬", "眼神如", 
                "眼神扫", "眼神看", "眼神盯", "眼神注视", "眼神凝视"
            ],
            "声音描写": [
                "声音冷", "声音狠", "声音发颤", "喉间压狠音", "声音沙哑", 
                "声音低沉", "声音高亢", "声音温柔", "声音严厉", "声音颤抖"
            ],
            "心理描写": [
                "心中暗爽", "很害怕", "心里想", "心想", "心中想", 
                "心里觉得", "心中觉得", "内心", "心里", "心中"
            ],
            "情感描述": [
                "气氛紧张", "很愤怒", "恐惧", "开心", "悲伤", 
                "兴奋", "焦虑", "紧张", "愤怒", "害怕"
            ],
            "抽象描述": [
                "很安静", "气质清雅", "优雅", "美丽", "丑陋", 
                "英俊", "丑陋", "高大", "矮小", "肥胖"
            ],
            "比喻": [
                "像什么", "如什么", "如诗如画", "如同", "宛如", 
                "仿佛", "好似", "恰似", "犹如", "好像"
            ],
            "形容词修饰": [
                "冷冷地", "狠狠地", "轻轻", "快速", "慢慢地", 
                "缓缓地", "重重地", "悄悄地", "偷偷地", "渐渐地"
            ]
        }
    
    def validate(self, script_content):
        """
        验证剧本内容
        
        Args:
            script_content (str): 剧本内容
            
        Returns:
            list: 验证问题列表
        """
        issues = []
        
        # 检查禁止的表达式
        for category, patterns in self.forbidden_patterns.items():
            for pattern in patterns:
                if pattern in script_content:
                    issues.append(f"[{category}] 禁止使用 '{pattern}'")
        
        # 检查台词括号中的眼神描写
        lines = script_content.split('\n')
        for i, line in enumerate(lines, 1):
            if '（眼神' in line or '(眼神' in line:
                issues.append(f"[台词括号] 第{i}行：禁止在台词括号中描写眼神")
        
        return issues
    
    def validate_file(self, file_path):
        """
        验证剧本文件
        
        Args:
            file_path (str): 剧本文件路径
            
        Returns:
            list: 验证问题列表
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            return self.validate(content)
        except Exception as e:
            return [f"读取文件失败: {e}"]
    
    def validate_directory(self, directory_path):
        """
        验证目录中的所有剧本文件
        
        Args:
            directory_path (str): 目录路径
            
        Returns:
            dict: 验证结果，键为文件名，值为问题列表
        """
        import os
        results = {}
        
        for filename in os.listdir(directory_path):
            if filename.endswith('.md'):
                file_path = os.path.join(directory_path, filename)
                issues = self.validate_file(file_path)
                results[filename] = issues
        
        return results
