# 人物解析器
# 负责解析人物.md文件，提取人物信息

from .markdown_parser import MarkdownParser

class CharacterParser:
    """
    人物解析器
    
    负责解析人物.md文件，提取人物信息
    """
    
    def __init__(self):
        """
        初始化人物解析器
        """
        self.md_parser = MarkdownParser()
    
    def parse_file(self, file_path):
        """
        解析人物.md文件
        
        Args:
            file_path (str): 文件路径
            
        Returns:
            dict: 人物字典，键为人物名称，值为人物信息
        """
        try:
            # 读取文件内容
            content = self.md_parser.parse_file(file_path)
            # 解析人物信息
            characters = self.parse_content(content)
            return characters
        except Exception as e:
            print(f"解析人物文件失败: {e}")
            return {}
    
    def parse_content(self, content):
        """
        解析人物文本内容
        
        Args:
            content (str): 人物文本内容
            
        Returns:
            dict: 人物字典
        """
        characters = {}
        lines = content.split('\n')
        current_character = None
        current_info = {}
        current_section = None
        
        for line in lines:
            line = line.strip()
            
            # 跳过空行
            if not line:
                continue
            
            # 检测人物类别（如「主角」、「核心配角」、「主要配角」等）
            if line.startswith('主角') or line.startswith('核心配角') or line.startswith('主要配角') or line.startswith('次要配角') or line.startswith('反派势力'):
                # 重置当前人物
                current_character = None
                current_info = {}
                current_section = line
            
            # 检测人物名称（如「陆念离」、「陆长乐」等）
            elif not current_character and not line.startswith('阶段') and not line.startswith('---'):
                # 新人物
                current_character = line
                current_info = {
                    "name": current_character,
                    "category": current_section,
                    "stages": {}
                }
            
            # 检测阶段信息（如「前期」、「中期」、「后期」等）
            elif line.startswith('阶段'):
                # 跳过表头
                pass
            
            # 检测人物阶段信息
            elif current_character and line:
                # 分割阶段信息
                parts = line.split('\t')
                if len(parts) >= 6:
                    stage = parts[0].strip()
                    identity = parts[1].strip()
                    background = parts[2].strip()
                    personality = parts[3].strip()
                    age = parts[4].strip()
                    appearance = parts[5].strip()
                    
                    # 保存阶段信息
                    current_info["stages"][stage] = {
                        "identity": identity,
                        "background": background,
                        "personality": personality,
                        "age": age,
                        "appearance": appearance
                    }
            
            # 检测分隔线
            elif line.startswith('---'):
                # 保存当前人物
                if current_character:
                    characters[current_character] = current_info
                # 重置
                current_character = None
                current_info = {}
        
        # 保存最后一个人物
        if current_character:
            characters[current_character] = current_info
        
        return characters
    
    def get_character(self, characters, name):
        """
        获取指定人物信息
        
        Args:
            characters (dict): 人物字典
            name (str): 人物名称
            
        Returns:
            dict: 人物信息或None
        """
        return characters.get(name)
    
    def get_character_stage(self, character, stage):
        """
        获取人物指定阶段的信息
        
        Args:
            character (dict): 人物信息
            stage (str): 阶段名称（如「前期」、「中期」、「后期」）
            
        Returns:
            dict: 阶段信息或None
        """
        if "stages" in character:
            return character["stages"].get(stage)
        return None
