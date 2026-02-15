# 一致性验证器
# 负责验证剧本内容与原文档的一致性

class ConsistencyValidator:
    """
    一致性验证器
    
    负责验证剧本内容与原文档的一致性，确保人物、场景、世界观等方面的一致性
    """
    
    def __init__(self, data_manager):
        """
        初始化一致性验证器
        
        Args:
            data_manager (DataManager): 数据管理器
        """
        self.data_manager = data_manager
    
    def validate(self, script_content, episode):
        """
        验证剧本内容
        
        Args:
            script_content (str): 剧本内容
            episode (int): 集数
            
        Returns:
            list: 验证问题列表
        """
        issues = []
        
        # 验证人物一致性
        character_issues = self.validate_characters(script_content)
        issues.extend(character_issues)
        
        # 验证场景一致性
        scene_issues = self.validate_scenes(script_content)
        issues.extend(scene_issues)
        
        # 验证剧情一致性
        outline_issues = self.validate_outline(script_content, episode)
        issues.extend(outline_issues)
        
        return issues
    
    def validate_characters(self, script_content):
        """
        验证人物一致性
        
        Args:
            script_content (str): 剧本内容
            
        Returns:
            list: 人物一致性问题列表
        """
        issues = []
        
        # 获取所有人物
        characters = self.data_manager.get_characters()
        character_names = list(characters.keys())
        
        # 检查出场人物是否在人物列表中
        # 这里简化处理，实际应该提取出场人物列表进行检查
        
        return issues
    
    def validate_scenes(self, script_content):
        """
        验证场景一致性
        
        Args:
            script_content (str): 剧本内容
            
        Returns:
            list: 场景一致性问题列表
        """
        issues = []
        
        # 获取所有场景
        scenes = self.data_manager.get_scenes()
        scene_names = list(scenes.keys())
        
        # 检查场景是否在场景列表中
        # 这里简化处理，实际应该提取场景列表进行检查
        
        return issues
    
    def validate_outline(self, script_content, episode):
        """
        验证剧情一致性
        
        Args:
            script_content (str): 剧本内容
            episode (int): 集数
            
        Returns:
            list: 剧情一致性问题列表
        """
        issues = []
        
        # 获取对应集数的剧情大纲
        outline = self.data_manager.get_outline(episode)
        if not outline:
            issues.append(f"第{episode}集剧情大纲不存在")
        
        return issues
    
    def validate_file(self, file_path, episode):
        """
        验证剧本文件
        
        Args:
            file_path (str): 剧本文件路径
            episode (int): 集数
            
        Returns:
            list: 验证问题列表
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            return self.validate(content, episode)
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
            if filename.endswith('.md') and filename.startswith('第') and '集' in filename:
                # 提取集数
                try:
                    episode = int(filename.split('第')[1].split('集')[0])
                except ValueError:
                    episode = 0
                
                file_path = os.path.join(directory_path, filename)
                issues = self.validate_file(file_path, episode)
                results[filename] = issues
        
        return results
