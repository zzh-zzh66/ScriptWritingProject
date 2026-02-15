# 格式验证器
# 负责验证剧本格式是否符合要求

class FormatValidator:
    """
    格式验证器
    
    负责验证剧本格式是否符合要求，包括场景格式、台词格式、音效标注格式等
    """
    
    def __init__(self):
        """
        初始化格式验证器
        """
        pass
    
    def validate(self, script_content):
        """
        验证剧本内容格式
        
        Args:
            script_content (str): 剧本内容
            
        Returns:
            list: 验证问题列表
        """
        issues = []
        
        # 检查剧本结构
        structure_issues = self.validate_structure(script_content)
        issues.extend(structure_issues)
        
        # 检查场景格式
        scene_issues = self.validate_scenes(script_content)
        issues.extend(scene_issues)
        
        # 检查台词格式
        dialogue_issues = self.validate_dialogues(script_content)
        issues.extend(dialogue_issues)
        
        # 检查音效标注格式
        sound_issues = self.validate_sound_effects(script_content)
        issues.extend(sound_issues)
        
        # 检查颜色标记格式
        color_issues = self.validate_color_markers(script_content)
        issues.extend(color_issues)
        
        return issues
    
    def validate_structure(self, script_content):
        """
        验证剧本结构
        
        Args:
            script_content (str): 剧本内容
            
        Returns:
            list: 结构问题列表
        """
        issues = []
        
        # 检查是否有标题
        if "第" not in script_content or "集：" not in script_content:
            issues.append("剧本缺少标题")
        
        # 检查是否有出场人物
        if "出场人物：" not in script_content:
            issues.append("剧本缺少出场人物")
        
        # 检查是否有场景列表
        if "场景列表：" not in script_content:
            issues.append("剧本缺少场景列表")
        
        return issues
    
    def validate_scenes(self, script_content):
        """
        验证场景格式
        
        Args:
            script_content (str): 剧本内容
            
        Returns:
            list: 场景格式问题列表
        """
        issues = []
        
        # 检查场景格式
        lines = script_content.split('\n')
        for i, line in enumerate(lines, 1):
            line = line.strip()
            if line and '-' in line and ('日' in line or '夜' in line) and ('内' in line or '外' in line):
                # 场景格式检查
                parts = line.split(' ')
                if len(parts) < 4:
                    issues.append(f"第{i}行：场景格式不正确，应为 '场景编号 时间 内外 场景名称'")
        
        return issues
    
    def validate_dialogues(self, script_content):
        """
        验证台词格式
        
        Args:
            script_content (str): 剧本内容
            
        Returns:
            list: 台词格式问题列表
        """
        issues = []
        
        # 检查台词格式
        lines = script_content.split('\n')
        for i, line in enumerate(lines, 1):
            line = line.strip()
            if line and ("（" in line or "(" in line) and "）" in line or ")" in line:
                # 检查台词括号中的内容是否符合要求
                if '（眼神' in line or '(眼神' in line:
                    issues.append(f"第{i}行：台词括号中禁止描写眼神")
                if '（声音' in line or '(声音' in line:
                    issues.append(f"第{i}行：台词括号中禁止描写声音")
        
        return issues
    
    def validate_sound_effects(self, script_content):
        """
        验证音效标注格式
        
        Args:
            script_content (str): 剧本内容
            
        Returns:
            list: 音效标注问题列表
        """
        issues = []
        
        # 检查音效标注格式
        lines = script_content.split('\n')
        for i, line in enumerate(lines, 1):
            line = line.strip()
            if line.startswith("声音提示："):
                # 音效标注格式检查
                if not line.endswith('\n'):
                    issues.append(f"第{i}行：音效标注应单独成段")
        
        return issues
    
    def validate_color_markers(self, script_content):
        """
        验证颜色标记格式
        
        Args:
            script_content (str): 剧本内容
            
        Returns:
            list: 颜色标记问题列表
        """
        issues = []
        
        # 检查颜色标记
        color_markers = ["【绿色】", "【黄色】", "【蓝色】"]
        marker_count = {}
        
        for marker in color_markers:
            count = script_content.count(marker)
            marker_count[marker] = count
        
        # 检查是否有绿色标记（高光场景）
        if marker_count.get("【绿色】", 0) < 1:
            issues.append("剧本缺少绿色标记（高光场景）")
        
        # 检查是否有黄色标记（冲突场景）
        if marker_count.get("【黄色】", 0) < 1:
            issues.append("剧本缺少黄色标记（冲突场景）")
        
        # 检查是否有蓝色标记（钩子场景）
        if marker_count.get("【蓝色】", 0) < 1:
            issues.append("剧本缺少蓝色标记（钩子场景）")
        
        return issues
    
    def validate_file(self, file_path):
        """
        验证剧本文件格式
        
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
        验证目录中的所有剧本文件格式
        
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
