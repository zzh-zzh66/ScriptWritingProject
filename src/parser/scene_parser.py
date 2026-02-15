# 场景解析器
# 负责解析场景列表.md文件，提取场景信息

from .markdown_parser import MarkdownParser

class SceneParser:
    """
    场景解析器
    
    负责解析场景列表.md文件，提取场景信息
    """
    
    def __init__(self):
        """
        初始化场景解析器
        """
        self.md_parser = MarkdownParser()
    
    def parse_file(self, file_path):
        """
        解析场景列表.md文件
        
        Args:
            file_path (str): 文件路径
            
        Returns:
            dict: 场景字典，键为场景名称，值为场景信息
        """
        try:
            # 读取文件内容
            content = self.md_parser.parse_file(file_path)
            # 解析场景信息
            scenes = self.parse_content(content)
            return scenes
        except Exception as e:
            print(f"解析场景文件失败: {e}")
            return {}
    
    def parse_content(self, content):
        """
        解析场景文本内容
        
        Args:
            content (str): 场景文本内容
            
        Returns:
            dict: 场景字典
        """
        scenes = {}
        lines = content.split('\n')
        current_category = None
        
        for line in lines:
            line = line.strip()
            
            # 跳过空行
            if not line:
                continue
            
            # 检测场景类别（如「核心场景」、「皇宫场景」、「长安城场景」等）
            if line.startswith('核心场景') or line.startswith('皇宫场景') or line.startswith('长安城场景') or line.startswith('战场场景') or line.startswith('密道场景') or line.startswith('边关场景') or line.startswith('其他场景') or line.startswith('终极场景'):
                current_category = line
            
            # 检测场景信息
            elif line.startswith('场景名'):
                # 跳过表头
                pass
            
            # 解析场景信息
            elif current_category and line:
                # 分割场景信息
                parts = line.split('\t')
                if len(parts) >= 3:
                    name = parts[0].strip()
                    time = parts[1].strip()
                    description = parts[2].strip()
                    
                    # 保存场景信息
                    scenes[name] = {
                        "name": name,
                        "category": current_category,
                        "time": time,
                        "description": description
                    }
        
        return scenes
    
    def get_scene(self, scenes, name):
        """
        获取指定场景信息
        
        Args:
            scenes (dict): 场景字典
            name (str): 场景名称
            
        Returns:
            dict: 场景信息或None
        """
        return scenes.get(name)
    
    def get_scenes_by_category(self, scenes, category):
        """
        获取指定类别的场景
        
        Args:
            scenes (dict): 场景字典
            category (str): 场景类别
            
        Returns:
            list: 场景列表
        """
        return [scene for scene in scenes.values() if scene.get("category") == category]
    
    def search_scenes(self, scenes, keyword):
        """
        搜索场景
        
        Args:
            scenes (dict): 场景字典
            keyword (str): 搜索关键词
            
        Returns:
            list: 匹配的场景列表
        """
        return [scene for scene in scenes.values() if keyword in scene.get("name", "") or keyword in scene.get("description", "")]
