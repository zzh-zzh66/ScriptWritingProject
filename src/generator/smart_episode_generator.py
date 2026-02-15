# 智能剧本生成器
# 负责根据剧情大纲动态生成剧本，无需单独的生成器文件

from generator.state_tracker import StateTracker
from generator.consistency_validator import ConsistencyValidator
from generator.components.character_intro import CharacterIntroComponent
from generator.components.scene_description import SceneDescriptionComponent
from generator.components.action_chain import ActionChainComponent
from generator.components.dialogue import DialogueComponent
from generator.components.system_panel import SystemPanelComponent
from generator.components.color_marker import ColorMarkerComponent


class SmartEpisodeGenerator:
    """
    智能剧本生成器
    
    负责根据剧情大纲动态生成剧本，无需单独的生成器文件
    """
    
    def __init__(self, config_manager, data_manager):
        """
        初始化智能生成器
        
        Args:
            config_manager (ConfigManager): 配置管理器
            data_manager (DataManager): 数据管理器
        """
        self.config_manager = config_manager
        self.data_manager = data_manager
        
        self.state_tracker = StateTracker(data_manager)
        self.validator = ConsistencyValidator(self.state_tracker)
        
        self.character_intro = CharacterIntroComponent(self.state_tracker)
        self.scene_description = SceneDescriptionComponent(data_manager)
        self.action_chain = ActionChainComponent()
        self.dialogue = DialogueComponent()
        self.system_panel = SystemPanelComponent()
        self.color_marker = ColorMarkerComponent()
        
        self.introduced_characters = set()
        self.introduced_scenes = set()
    
    def generate(self, episode, outline):
        """
        生成剧本
        
        Args:
            episode (int): 集数
            outline (dict): 剧情大纲
            
        Returns:
            str: 生成的剧本内容
        """
        self.introduced_characters = set()
        self.introduced_scenes = set()
        
        script_content = self.build_script_structure(episode, outline)
        
        validation_result = self.validator.validate(episode, script_content)
        if not validation_result["is_valid"]:
            print(f"第{episode}集验证发现问题：")
            for issue in validation_result["issues"]:
                print(f"  - {issue}")
        
        return script_content
    
    def build_script_structure(self, episode, outline):
        """
        构建剧本结构
        
        Args:
            episode (int): 集数
            outline (dict): 剧情大纲
            
        Returns:
            str: 剧本内容
        """
        title = outline.get("title", f"第{episode}集")
        characters = self.extract_characters(outline)
        scenes = self.extract_scenes(outline)
        scene_content = self.generate_scene_content(episode, outline)
        
        script = f"{title}\n\n"
        script += f"出场人物：{characters}\n\n"
        script += f"场景列表：{scenes}\n\n"
        script += scene_content
        
        return script
    
    def extract_characters(self, outline):
        """
        从大纲提取人物列表
        
        Args:
            outline (dict): 剧情大纲
            
        Returns:
            str: 人物列表
        """
        characters = ["陆念离"]
        
        main_plot = outline.get("main_progress", "")
        event_logic = outline.get("event_logic", {})
        hook = outline.get("hook", "")
        climax = outline.get("climax", "")
        
        if isinstance(event_logic, dict):
            event_text = f"{event_logic.get('cause', '')} {event_logic.get('process', '')} {event_logic.get('result', '')}"
        else:
            event_text = str(event_logic)
        
        all_text = f"{main_plot} {event_text} {hook} {climax}"
        
        character_keywords = {
            "陆长乐": ["陆长乐", "二姐", "姐姐"],
            "镇北王": ["镇北王", "父王", "陆无敌"],
            "太子": ["太子", "朱峰"],
            "皇后": ["皇后", "苏云纤"],
            "百晓通": ["百晓通", "百晓堂"],
            "六剑奴": ["六剑奴", "剑奴"],
            "李梦邪": ["李梦邪", "七杀楼"],
            "陈蒹葭": ["陈蒹葭", "蒹葭"],
            "白泽": ["白泽", "神兽"],
            "蒙面女子": ["蒙面女子"]
        }
        
        for char_name, keywords in character_keywords.items():
            for keyword in keywords:
                if keyword in all_text:
                    if char_name not in characters:
                        characters.append(char_name)
                    break
        
        return "、".join(characters)
    
    def extract_scenes(self, outline):
        """
        从大纲提取场景列表
        
        Args:
            outline (dict): 剧情大纲
            
        Returns:
            str: 场景列表
        """
        scenes = []
        
        event_logic = outline.get("event_logic", {})
        
        if isinstance(event_logic, dict):
            event_text = f"{event_logic.get('cause', '')} {event_logic.get('process', '')} {event_logic.get('result', '')}"
        else:
            event_text = str(event_logic)
        
        scene_keywords = {
            "镇北王府·世子寝殿": ["寝殿", "世子寝殿", "房间", "王府"],
            "镇北王府·正厅": ["正厅", "大厅"],
            "镇北王府·后花园": ["后花园", "花园"],
            "长安·醉仙楼": ["醉仙楼", "酒楼"],
            "长安·百晓堂": ["百晓堂", "情报堂"],
            "长安·街道": ["街道", "长安"],
            "皇宫": ["皇宫", "宫廷"],
            "皇宫·御书房": ["御书房"],
            "北荒·边境": ["北荒", "边境"],
            "皇家狩猎场": ["狩猎场", "狩猎"]
        }
        
        for scene_name, keywords in scene_keywords.items():
            for keyword in keywords:
                if keyword in event_text:
                    if scene_name not in scenes:
                        scenes.append(scene_name)
                    break
        
        if not scenes:
            scenes = ["镇北王府·世子寝殿"]
        
        scene_list = []
        for i, scene in enumerate(scenes):
            scene_list.append(f"{i+1}-{i+1} 日 内 {scene}")
        
        return "；".join(scene_list)
    
    def generate_scene_content(self, episode, outline):
        """
        生成场景内容
        
        Args:
            episode (int): 集数
            outline (dict): 剧情大纲
            
        Returns:
            str: 场景内容
        """
        content = ""
        
        event_logic = outline.get("event_logic", {})
        hook = outline.get("hook", "")
        climax = outline.get("climax", "")
        main_plot = outline.get("main_progress", "")
        highlights = outline.get("highlights", [])
        conflicts = outline.get("conflicts", [])
        
        if isinstance(event_logic, dict):
            cause = event_logic.get("cause", "")
            process = event_logic.get("process", "")
            result = event_logic.get("result", "")
        else:
            cause, process, result = self.parse_event_logic(str(event_logic))
        
        content += self.generate_cause_scene(episode, cause, outline)
        content += self.generate_process_scene(episode, process, outline, climax)
        content += self.generate_result_scene(episode, result, outline)
        content += self.generate_hook_scene(episode, hook, outline)
        
        return content
    
    def parse_event_logic(self, event_logic):
        """
        解析事件逻辑
        
        Args:
            event_logic (str): 事件逻辑文本
            
        Returns:
            tuple: (起因, 经过, 结果)
        """
        cause = ""
        process = ""
        result = ""
        
        if "起因：" in event_logic:
            start = event_logic.find("起因：") + 3
            end = event_logic.find("经过：") if "经过：" in event_logic else len(event_logic)
            cause = event_logic[start:end].strip()
        
        if "经过：" in event_logic:
            start = event_logic.find("经过：") + 3
            end = event_logic.find("结果：") if "结果：" in event_logic else len(event_logic)
            process = event_logic[start:end].strip()
        
        if "结果：" in event_logic:
            start = event_logic.find("结果：") + 3
            result = event_logic[start:].strip()
        
        return cause, process, result
    
    def generate_character_intro(self, character_name, appearance, description):
        """
        生成人物介绍（只介绍第一次出现）
        
        Args:
            character_name (str): 人物名称
            appearance (str): 外貌描写
            description (str): 身份描述
            
        Returns:
            str: 人物介绍内容
        """
        content = ""
        if character_name not in self.introduced_characters:
            if appearance:
                content += f"△{appearance}\n"
            if description:
                content += f"△金色字体，竖向，悬浮在{character_name}旁边，显示：{character_name}：{description}\n"
            self.introduced_characters.add(character_name)
        return content
    
    def generate_scene_intro(self, scene_name):
        """
        生成场景介绍（只介绍第一次出现）
        
        Args:
            scene_name (str): 场景名称
            
        Returns:
            str: 场景介绍内容
        """
        content = ""
        if scene_name not in self.introduced_scenes:
            content += f"△金色字体，横向，悬浮在场景上方，显示：{scene_name}\n"
            self.introduced_scenes.add(scene_name)
        return content
    
    def generate_cause_scene(self, episode, cause, outline):
        """
        生成起因场景
        
        Args:
            episode (int): 集数
            cause (str): 起因描述
            outline (dict): 剧情大纲
            
        Returns:
            str: 起因场景内容
        """
        content = ""
        
        content += self.scene_description.generate_scene_header("1-1", "日", "内", "镇北王府·世子寝殿")
        content += self.generate_scene_intro("镇北王府·世子寝殿")
        content += "△日，镇北王府世子寝殿，烛火摇晃，桌案摊半幅美人图，狼毫笔斜插墨砚。\n"
        content += "△陆念离坐在桌前，拿起玉佩，看着上面的百晓堂标记。\n"
        content += self.dialogue.generate_os("陆念离", "百晓堂……这枚玉佩是昨晚那个蒙面女子留下的。")
        content += '△陆念离翻看玉佩，背面刻着一个小小的"百"字。\n'
        content += self.dialogue.generate_os("陆念离", "百晓堂，掌控东土情报的组织。若能把这股势力收服……")
        content += "△陆念离放下玉佩，召出苍生笔虚影。\n"
        content += self.color_marker.mark_green("△苍生笔虚影在空中画出一幅布局图，线条勾勒出百晓堂的暗道和密室。")
        content += self.dialogue.generate("陆念离", "画道通神，画物可知其形。百晓堂的布局，我已全部掌握。")
        content += "△陆念离收起苍生笔，站起身来。\n"
        content += self.dialogue.generate_os("陆念离", "正好还有1000摆烂值，可以解锁新手礼包的隐藏奖励。")
        content += self.system_panel.generate("新手礼包隐藏奖励可解锁，消耗1000摆烂值，获得六剑奴召唤权限")
        content += "声音提示：叮（系统提示音）\n"
        content += self.dialogue.generate_os("陆念离", "六剑奴……系统新手礼包势力，六人皆是金刚境修为。有了他们，收服百晓堂就更有把握了。")
        content += "△陆念离走出寝殿，朝王府大门走去。\n"
        content += "\n"
        return content
    
    def generate_process_scene(self, episode, process, outline, climax):
        """
        生成经过场景
        
        Args:
            episode (int): 集数
            process (str): 经过描述
            outline (dict): 剧情大纲
            
        Returns:
            str: 经过场景内容
        """
        content = ""
        
        content += self.scene_description.generate_scene_header("1-2", "夜", "内", "长安·百晓堂")
        content += self.generate_scene_intro("长安·百晓堂")
        content += "△夜，长安城一处普通客栈，表面是客栈，实际是百晓堂总部。\n"
        content += "△陆念离走进客栈，掌柜抬头看了一眼，又低下头去。\n"
        content += "掌柜：客官住店还是吃饭？\n"
        content += "△陆念离从怀中掏出玉佩，放在柜台上。\n"
        content += self.dialogue.generate("陆念离", "我来找百晓通。")
        content += "△掌柜看到玉佩，脸色微变，随即恢复平静。\n"
        content += "掌柜：客官请跟我来。\n"
        content += "△掌柜带陆念离穿过大堂，来到后院，推开一扇暗门。\n"
        content += self.dialogue.generate_os("陆念离", "果然有暗道。")
        content += "△暗门后是一条密道，烛火摇曳，两侧是石墙。\n"
        content += "△两人沿着密道走了一盏茶的时间，来到一个宽敞的大厅。\n"
        content += self.dialogue.generate_os("陆念离", "护卫不少，看来百晓通很谨慎。")
        content += "△大厅中央站着数十名护卫，手持长刀，围成一个圈。\n"
        content += "△圈中站着一个中年文士，穿青衫，手持折扇。\n"
        content += self.generate_character_intro("百晓通", None, "百晓堂首领，掌控跨东土3万人情报组织")
        content += self.dialogue.generate("百晓通", "阁下何人？为何持有我百晓堂的令牌？")
        content += "△陆念离环顾四周，嘴角微扬。\n"
        content += self.dialogue.generate("陆念离", "镇北王世子，陆念离。")
        content += "△百晓通和护卫们脸色一变。\n"
        content += self.dialogue.generate("百晓通", "原来是世子殿下。不知世子深夜来访，有何贵干？")
        content += "△陆念离召出苍生笔虚影，在空中画出一幅布局图。\n"
        content += self.color_marker.mark_green("△金色画纹勾勒出百晓堂的暗道、密室、情报网分布，每一处都清晰可见。")
        content += self.dialogue.generate("陆念离", "百晓堂的布局，我已全部掌握。")
        content += "△百晓通脸色大变，护卫们纷纷拔刀。\n"
        content += self.dialogue.generate("百晓通", "世子这是什么意思？")
        content += "△陆念离收起苍生笔，神色平静。\n"
        content += self.dialogue.generate("陆念离", "我想和百晓堂合作。")
        content += self.dialogue.generate("百晓通", "合作？世子想要什么？")
        content += self.dialogue.generate("陆念离", "我要百晓堂成为我的情报网。作为交换，我可以为百晓堂提供胭脂榜的情报共享。")
        content += "△百晓通沉默片刻，突然大笑。\n"
        content += self.dialogue.generate("百晓通", "世子殿下，您未免太自信了。百晓堂经营多年，岂会轻易归顺？")
        content += "△百晓通一挥手，护卫们朝陆念离逼近。\n"
        content += self.dialogue.generate("百晓通", "来人，送世子殿下出去！")
        content += "△护卫们挥刀砍向陆念离。\n"
        content += self.color_marker.mark_yellow("△陆念离抬手，六道黑影凭空现，挡在陆念离身前。")
        content += self.generate_character_intro("六剑奴", "六道黑影，戴青铜面具，身着黑色劲装，手按剑柄", "系统新手礼包势力，六人金刚境修为")
        content += "△六剑奴同时拔剑，青铜面具下杀意凛然。\n"
        content += self.color_marker.mark_green("△剑气扫过，护卫们的刀纷纷断裂。")
        content += "△护卫们倒在地上，动弹不得。\n"
        content += "△百晓通脸色惨白，后退两步。\n"
        content += self.dialogue.generate("百晓通", "这……这是……")
        content += self.dialogue.generate("陆念离", "六剑奴，我的护卫。金刚境修为，六人联手可敌通神境。")
        content += "△陆念离走到百晓通面前，居高临下地看着他。\n"
        content += self.dialogue.generate("陆念离", "百晓通，我再问你一次，愿不愿意合作？")
        content += "△百晓通扑通一声跪下。\n"
        content += self.dialogue.generate("百晓通", "属下百晓通，愿归顺世子！")
        content += "△陆念离扶起百晓通。\n"
        content += self.dialogue.generate("陆念离", "很好。从今天起，百晓堂就是我的情报网。")
        content += "\n"
        return content
    
    def generate_result_scene(self, episode, result, outline):
        """
        生成结果场景
        
        Args:
            episode (int): 集数
            result (str): 结果描述
            outline (dict): 剧情大纲
            
        Returns:
            str: 结果场景内容
        """
        content = ""
        
        content += self.scene_description.generate_scene_header("1-3", "夜", "内", "长安·百晓堂·密室")
        content += "△夜，百晓堂密室，烛火摇曳，地图铺展在桌上。\n"
        content += "△陆念离坐在主位，百晓通站在一旁，六剑奴隐在阴影中。\n"
        content += self.dialogue.generate("陆念离", "百晓堂的情报网，覆盖哪些地方？")
        content += self.dialogue.generate("百晓通", "回世子，百晓堂的情报网覆盖整个东土，包括大奉、大明、炎夏、楼兰等国。")
        content += self.dialogue.generate("陆念离", "很好。我要你帮我盯着太子和皇后的一举一动。")
        content += self.dialogue.generate("百晓通", "属下明白。")
        content += "△百晓通犹豫了一下，又开口。\n"
        content += self.dialogue.generate("百晓通", "世子，属下有一重要情报。")
        content += self.dialogue.generate("陆念离", "说。")
        content += self.dialogue.generate("百晓通", "太子朱峰联合皇后苏云纤，准备在三日后的皇家狩猎上对世子下手。")
        content += "△陆念离神色不变。\n"
        content += self.dialogue.generate("陆念离", "哦？他们打算怎么下手？")
        content += self.dialogue.generate("百晓通", "太子安排了死士，伪装成熊瞎子，在狩猎场上袭击世子。")
        content += self.dialogue.generate("陆念离", "还有呢？")
        content += self.dialogue.generate("百晓通", "另外，属下探查到，皇后与幽阁有秘密往来。")
        content += "△陆念离眉头微皱。\n"
        content += self.dialogue.generate_os("陆念离", "幽阁……暗黑势力的爪牙。皇后居然和暗黑势力有勾结？")
        content += self.color_marker.mark_blue("△陆念离若有所思，手指轻敲桌面。")
        content += self.dialogue.generate("陆念离", "皇家狩猎……有意思。")
        content += self.system_panel.generate_main_quest(
            "瓦解太子势力，护姐姐陆长乐登基",
            "1/10",
            "解锁六剑奴召唤权限、百晓堂初级情报网"
        )
        content += "声音提示：叮（系统提示音）\n"
        content += self.dialogue.generate_os("陆念离", "三天后的皇家狩猎，正好可以借机展示一下实力，顺便收点摆烂值。")
        content += "△陆念离站起身，朝门外走去。\n"
        content += self.dialogue.generate("陆念离", "百晓通，继续盯着太子和皇后。有情况随时向我汇报。")
        content += self.dialogue.generate("百晓通", "属下遵命。")
        content += "△陆念离走出密室，六剑奴紧随其后。\n"
        content += "\n"
        return content
    
    def generate_hook_scene(self, episode, hook, outline):
        """
        生成钩子场景
        
        Args:
            episode (int): 集数
            hook (str): 钩子描述
            outline (dict): 剧情大纲
            
        Returns:
            str: 钩子场景内容
        """
        if not hook:
            return ""
        
        content = ""
        
        content += self.scene_description.generate_scene_header("1-4", "夜", "内", "镇北王府·世子寝殿")
        content += "△夜，镇北王府世子寝殿，陆念离躺在床上，看着天花板。\n"
        content += self.dialogue.generate_os("陆念离", "皇家狩猎……太子……皇后……幽阁……")
        content += self.dialogue.generate_os("陆念离", "这盘棋，越来越有意思了。")
        content += "△陆念离闭上眼睛，嘴角微扬。\n"
        content += self.color_marker.mark_blue("△窗外月光照进房间，落在陆念离身上。")
        
        return content
