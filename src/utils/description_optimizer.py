# 描写优化器
# 将描写优化为AI可直接生成画面的提示词

class SceneOptimizer:
    """
    场景描写优化器
    
    优化场景描写为"时间+地点+物品+状态"格式
    """
    
    def optimize(self, description):
        """
        优化场景描写
        
        Args:
            description (str): 原始场景描写
            
        Returns:
            str: 优化后的场景描写
        """
        # 移除抽象描述和比喻
        optimized = self.remove_abstract_and_metaphor(description)
        
        # 简化为"时间+地点+物品+状态"格式
        optimized = self.simplify_format(optimized)
        
        return optimized
    
    def remove_abstract_and_metaphor(self, text):
        """
        移除抽象描述和比喻
        
        Args:
            text (str): 原始文本
            
        Returns:
            str: 移除后的文本
        """
        # 移除常见的抽象描述词
        abstract_words = ["很安静", "气氛", "氛围", "感觉", "仿佛", "好像", "如同", "宛如"]
        for word in abstract_words:
            text = text.replace(word, "")
        
        # 移除常见的比喻词
        metaphor_words = ["如诗如画", "如刀", "如炬", "如星", "如", "像"]
        for word in metaphor_words:
            text = text.replace(word, "")
        
        return text
    
    def simplify_format(self, text):
        """
        简化为"时间+地点+物品+状态"格式
        
        Args:
            text (str): 原始文本
            
        Returns:
            str: 简化后的文本
        """
        # 移除啰嗦的描述
        text = text.replace("在夜风里晃", "摇晃")
        text = text.replace("在夜风中晃", "摇晃")
        text = text.replace("在夜风中", "")
        
        # 移除重复的描述
        text = text.replace("，，", "，")
        text = text.replace("，，", "，")
        
        return text.strip()


class ActionOptimizer:
    """
    动作描写优化器
    
    优化动作描写为"主体+动词+对象"结构
    """
    
    def optimize(self, action):
        """
        优化动作描写
        
        Args:
            action (str): 原始动作描写
            
        Returns:
            str: 优化后的动作描写
        """
        # 移除形容词和副词修饰
        optimized = self.remove_modifiers(action)
        
        # 拆解为连贯步骤
        optimized = self.break_down_steps(optimized)
        
        # 补充动态细节
        optimized = self.add_dynamic_details(optimized)
        
        return optimized
    
    def remove_modifiers(self, text):
        """
        移除形容词和副词修饰
        
        Args:
            text (str): 原始文本
            
        Returns:
            str: 移除后的文本
        """
        # 移除常见的副词
        modifiers = ["冷冷地", "狠狠地", "轻轻地", "快速地", "慢慢地", "缓缓地", "重重地", "悄悄地", "偷偷地", "渐渐地"]
        for modifier in modifiers:
            text = text.replace(modifier, "")
        
        # 移除常见的形容词修饰
        text = text.replace("冷冷地", "")
        text = text.replace("狠狠地", "")
        text = text.replace("轻轻地", "")
        
        return text
    
    def break_down_steps(self, text):
        """
        拆解为连贯步骤
        
        Args:
            text (str): 原始文本
            
        Returns:
            str: 拆解后的文本
        """
        # 将长句拆解为短句
        # 这里只是基础处理，实际需要更复杂的逻辑
        return text
    
    def add_dynamic_details(self, text):
        """
        补充动态细节
        
        Args:
            text (str): 原始文本
            
        Returns:
            str: 补充细节后的文本
        """
        # 为动作补充动态细节
        # 这里只是基础处理，实际需要更复杂的逻辑
        return text


class CharacterDetailOptimizer:
    """
    人物细节优化器
    
    优化人物细节为"外貌+简单的表情"
    """
    
    def optimize(self, detail):
        """
        优化人物细节
        
        Args:
            detail (str): 原始人物细节
            
        Returns:
            str: 优化后的人物细节
        """
        # 移除抽象描述
        optimized = self.remove_abstract_description(detail)
        
        # 聚焦可视觉识别的内容
        optimized = self.focus_on_visual_content(optimized)
        
        return optimized
    
    def remove_abstract_description(self, text):
        """
        移除抽象描述
        
        Args:
            text (str): 原始文本
            
        Returns:
            str: 移除后的文本
        """
        # 移除常见的抽象描述词
        abstract_words = ["气质清雅", "气质", "优雅", "美丽", "丑陋", "英俊", "高大", "矮小", "肥胖"]
        for word in abstract_words:
            text = text.replace(word, "")
        
        return text
    
    def focus_on_visual_content(self, text):
        """
        聚焦可视觉识别的内容
        
        Args:
            text (str): 原始文本
            
        Returns:
            str: 聚焦后的文本
        """
        # 聚焦外貌和简单表情
        # 这里只是基础处理，实际需要更复杂的逻辑
        return text


class DescriptionOptimizer:
    """
    描写优化器
    
    整合所有描写优化功能
    """
    
    def __init__(self):
        """
        初始化描写优化器
        """
        self.scene_optimizer = SceneOptimizer()
        self.action_optimizer = ActionOptimizer()
        self.character_optimizer = CharacterDetailOptimizer()
    
    def optimize_scene(self, description):
        """
        优化场景描写
        
        Args:
            description (str): 原始场景描写
            
        Returns:
            str: 优化后的场景描写
        """
        return self.scene_optimizer.optimize(description)
    
    def optimize_action(self, action):
        """
        优化动作描写
        
        Args:
            action (str): 原始动作描写
            
        Returns:
            str: 优化后的动作描写
        """
        return self.action_optimizer.optimize(action)
    
    def optimize_character(self, detail):
        """
        优化人物细节
        
        Args:
            detail (str): 原始人物细节
            
        Returns:
            str: 优化后的人物细节
        """
        return self.character_optimizer.optimize(detail)
    
    def optimize_all(self, text):
        """
        优化所有描写
        
        Args:
            text (str): 原始文本
            
        Returns:
            str: 优化后的文本
        """
        # 移除所有禁止事项
        text = self.remove_all_forbidden(text)
        
        # 优化场景描写
        text = self.optimize_scene(text)
        
        # 优化动作描写
        text = self.optimize_action(text)
        
        # 优化人物细节
        text = self.optimize_character(text)
        
        return text
    
    def remove_all_forbidden(self, text):
        """
        移除所有禁止事项
        
        Args:
            text (str): 原始文本
            
        Returns:
            str: 移除后的文本
        """
        # 移除眼神描写
        eye_phrases = ["眼神冷", "眼神锐利", "眼神一冷", "眼神扫过", "眼神没离开", "眼神坚定", "眼神警惕"]
        for phrase in eye_phrases:
            text = text.replace(phrase, "")
        
        # 移除声音描写
        sound_phrases = ["声音冷", "声音狠", "声音发颤", "喉间压狠音", "声音沙哑"]
        for phrase in sound_phrases:
            text = text.replace(phrase, "")
        
        # 移除心理描写
        mind_phrases = ["心中暗爽", "很害怕", "心里想", "心中想"]
        for phrase in mind_phrases:
            text = text.replace(phrase, "")
        
        # 移除情感描述
        emotion_phrases = ["气氛紧张", "很愤怒", "恐惧", "开心", "悲伤"]
        for phrase in emotion_phrases:
            text = text.replace(phrase, "")
        
        # 移除抽象描述
        abstract_phrases = ["很安静", "气质清雅", "优雅", "美丽"]
        for phrase in abstract_phrases:
            text = text.replace(phrase, "")
        
        # 移除比喻
        metaphor_phrases = ["像什么", "如什么", "如诗如画", "如同", "宛如", "仿佛"]
        for phrase in metaphor_phrases:
            text = text.replace(phrase, "")
        
        # 移除形容词和副词修饰
        modifier_phrases = ["冷冷地", "狠狠地", "轻轻地", "快速地", "慢慢地"]
        for phrase in modifier_phrases:
            text = text.replace(phrase, "")
        
        return text