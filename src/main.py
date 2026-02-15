#!/usr/bin/env python3
# 主入口文件
# 负责协调各个模块的工作，是整个项目的入口点

import argparse
import os
from utils.config_manager import ConfigManager
from utils.scene_selector import SceneSelector
from utils.character_manager import CharacterManager
from data.data_manager import DataManager
from parser.markdown_parser import MarkdownParser
from parser.character_parser import CharacterParser
from parser.scene_parser import SceneParser
from parser.outline_parser import OutlineParser
from parser.setting_parser import SettingParser
from generator.script_generator import ScriptGenerator

class Main:
    """
    主类
    
    负责协调各个模块的工作，是整个项目的入口点
    """
    
    def __init__(self):
        """
        初始化主类
        """
        # 初始化配置管理器
        self.config_manager = ConfigManager()
        # 初始化数据管理器
        self.data_manager = DataManager()
        # 初始化解析器
        self.markdown_parser = MarkdownParser()
        self.character_parser = CharacterParser()
        self.scene_parser = SceneParser()
        self.outline_parser = OutlineParser()
        self.setting_parser = SettingParser()
        # 初始化生成器
        self.script_generator = ScriptGenerator(self.config_manager, self.data_manager)
    
    def parse_documents(self):
        """
        解析所有文档
        """
        print("开始解析文档...")
        
        # 解析人物文档
        character_file = "doc/人物.md"
        if os.path.exists(character_file):
            characters = self.character_parser.parse_file(character_file)
            self.data_manager.set_characters(characters)
            print(f"解析人物文档完成，共解析 {len(characters)} 个角色")
        else:
            print(f"人物文档不存在: {character_file}")
        
        # 解析场景文档
        scene_file = "doc/场景列表.md"
        if os.path.exists(scene_file):
            scenes = self.scene_parser.parse_file(scene_file)
            self.data_manager.set_scenes(scenes)
            print(f"解析场景文档完成，共解析 {len(scenes)} 个场景")
        else:
            print(f"场景文档不存在: {scene_file}")
        
        # 解析剧情大纲
        outline_dir = "doc/剧情大纲"
        if os.path.exists(outline_dir):
            outlines = self.outline_parser.parse_directory(outline_dir)
            # 过滤掉summary，只保留集数大纲
            episode_outlines = {k: v for k, v in outlines.items() if isinstance(k, int)}
            self.data_manager.set_outlines(episode_outlines)
            print(f"解析剧情大纲完成，共解析 {len(episode_outlines)} 集大纲")
        else:
            print(f"剧情大纲目录不存在: {outline_dir}")
        
        # 解析设定文档
        setting_file = "doc/设定.md"
        if os.path.exists(setting_file):
            settings = self.setting_parser.parse_file(setting_file)
            self.data_manager.set_settings(settings)
            print("解析设定文档完成")
        else:
            print(f"设定文档不存在: {setting_file}")
        
        print("文档解析完成！")
    
    def generate_script(self, episode):
        """
        生成指定集数的剧本
        
        Args:
            episode (int): 集数
        """
        print(f"开始生成第{episode}集剧本...")
        script_content = self.script_generator.generate_script(episode)
        print(f"第{episode}集剧本生成完成！")
        print(f"剧本已保存到: {self.config_manager.get_output_dir()}/第{episode}集.md")
    
    def generate_all_scripts(self, start_episode=1, end_episode=70):
        """
        生成所有集数的剧本
        
        Args:
            start_episode (int): 开始集数
            end_episode (int): 结束集数
        """
        print(f"开始生成第{start_episode}集到第{end_episode}集的剧本...")
        self.script_generator.generate_all_scripts(start_episode, end_episode)
        print(f"所有剧本生成完成！")
        print(f"剧本已保存到: {self.config_manager.get_output_dir()}")
    
    def run(self):
        """
        运行主程序
        """
        # 解析命令行参数
        parser = argparse.ArgumentParser(description="AI漫剧剧本生成器")
        parser.add_argument("--generate", type=int, help="生成指定集数的剧本")
        parser.add_argument("--generate-all", action="store_true", help="生成所有集数的剧本")
        parser.add_argument("--start-episode", type=int, default=1, help="开始集数")
        parser.add_argument("--end-episode", type=int, default=70, help="结束集数")
        parser.add_argument("--parse", action="store_true", help="解析所有文档")
        parser.add_argument("--version", action="store_true", help="显示版本信息")
        
        args = parser.parse_args()
        
        # 显示版本信息
        if args.version:
            print(f"AI漫剧剧本生成器 v{self.config_manager.get_project_version()}")
            return
        
        # 解析文档
        if args.parse:
            self.parse_documents()
            return
        
        # 解析文档（默认）
        self.parse_documents()
        
        # 生成指定集数的剧本
        if args.generate:
            self.generate_script(args.generate)
        
        # 生成所有集数的剧本
        elif args.generate_all:
            self.generate_all_scripts(args.start_episode, args.end_episode)
        
        # 默认行为
        else:
            print("请指定要执行的操作：")
            print("  --generate <episode>    生成指定集数的剧本")
            print("  --generate-all         生成所有集数的剧本")
            print("  --parse                仅解析文档")
            print("  --version              显示版本信息")
            print("\n示例：")
            print("  python src/main.py --generate 1     # 生成第1集剧本")
            print("  python src/main.py --generate-all  # 生成所有70集剧本")

if __name__ == "__main__":
    # 创建主实例并运行
    main = Main()
    main.run()
