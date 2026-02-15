# Markdown解析器
# 负责解析Markdown文件，提取文本内容

class MarkdownParser:
    """
    Markdown解析器
    
    负责解析Markdown文件，提取文本内容
    """
    
    def __init__(self):
        """
        初始化Markdown解析器
        """
        pass
    
    def parse_file(self, file_path):
        """
        解析Markdown文件
        
        Args:
            file_path (str): 文件路径
            
        Returns:
            str: 文件内容
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            return content
        except Exception as e:
            print(f"解析Markdown文件失败: {e}")
            return ""
    
    def parse_text(self, text):
        """
        解析Markdown文本
        
        Args:
            text (str): Markdown文本
            
        Returns:
            str: 解析后的文本
        """
        # 这里可以添加更复杂的Markdown解析逻辑
        # 目前只是返回原始文本
        return text
    
    def extract_sections(self, content):
        """
        提取Markdown文本中的章节
        
        Args:
            content (str): Markdown文本
            
        Returns:
            dict: 章节字典，键为章节标题，值为章节内容
        """
        sections = {}
        lines = content.split('\n')
        current_section = None
        current_content = []
        
        for line in lines:
            # 检测章节标题（# 开头）
            if line.startswith('#'):
                # 如果有当前章节，保存
                if current_section:
                    sections[current_section] = '\n'.join(current_content)
                # 新章节
                current_section = line.strip('# ').strip()
                current_content = []
            else:
                # 章节内容
                current_content.append(line)
        
        # 保存最后一个章节
        if current_section:
            sections[current_section] = '\n'.join(current_content)
        
        return sections
    
    def extract_code_blocks(self, content):
        """
        提取Markdown文本中的代码块
        
        Args:
            content (str): Markdown文本
            
        Returns:
            list: 代码块列表
        """
        code_blocks = []
        in_code_block = False
        current_block = []
        
        for line in content.split('\n'):
            if line.startswith('```'):
                if in_code_block:
                    # 代码块结束
                    code_blocks.append('\n'.join(current_block))
                    current_block = []
                    in_code_block = False
                else:
                    # 代码块开始
                    in_code_block = True
            elif in_code_block:
                current_block.append(line)
        
        return code_blocks
