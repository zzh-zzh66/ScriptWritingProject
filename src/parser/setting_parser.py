# 设定解析器
# 负责解析设定.md文件，提取核心设定信息

from .markdown_parser import MarkdownParser

class SettingParser:
    """
    设定解析器
    
    负责解析设定.md文件，提取核心设定信息
    """
    
    def __init__(self):
        """
        初始化设定解析器
        """
        self.md_parser = MarkdownParser()
    
    def parse_file(self, file_path):
        """
        解析设定.md文件
        
        Args:
            file_path (str): 文件路径
            
        Returns:
            dict: 设定字典，包含金手指、世界观、主角人设等信息
        """
        try:
            # 读取文件内容
            content = self.md_parser.parse_file(file_path)
            # 解析设定信息
            settings = self.parse_content(content)
            return settings
        except Exception as e:
            print(f"解析设定文件失败: {e}")
            return {}
    
    def parse_content(self, content):
        """
        解析设定文本内容
        
        Args:
            content (str): 设定文本内容
            
        Returns:
            dict: 设定字典
        """
        settings = {}
        
        # 提取章节
        sections = self.md_parser.extract_sections(content)
        
        # 解析金手指设定
        if "金手指：画道通神系统（核心爽点引擎）" in sections:
            settings["golden_finger"] = self.parse_golden_finger(sections["金手指：画道通神系统（核心爽点引擎）"])
        
        # 解析世界观设定
        if "世界观设定（架空玄幻+权谋争霸双融合）" in sections:
            settings["worldview"] = self.parse_worldview(sections["世界观设定（架空玄幻+权谋争霸双融合）"])
        
        # 解析主角人设
        if "主角人设：陆念离（反差感拉满的爆款人设）" in sections:
            settings["protagonist"] = self.parse_protagonist(sections["主角人设：陆念离（反差感拉满的爆款人设）"])
        
        # 解析核心冲突
        if "核心冲突（七阶段层级递进，节奏紧凑）" in sections:
            settings["core_conflicts"] = self.parse_core_conflicts(sections["核心冲突（七阶段层级递进，节奏紧凑）"])
        
        # 解析新颖差异化设定
        if "新颖差异化设定（漫剧爆款核心亮点）" in sections:
            settings["differentiation"] = self.parse_differentiation(sections["新颖差异化设定（漫剧爆款核心亮点）"])
        
        # 解析核心爽点逻辑
        if "核心爽点逻辑（适配AIGC漫剧工业化）" in sections:
            settings["pleasure_logic"] = self.parse_pleasure_logic(sections["核心爽点逻辑（适配AIGC漫剧工业化）"])
        
        return settings
    
    def parse_golden_finger(self, content):
        """
        解析金手指设定
        
        Args:
            content (str): 金手指文本内容
            
        Returns:
            dict: 金手指设定
        """
        golden_finger = {}
        lines = content.split('\n')
        
        for line in lines:
            line = line.strip()
            
            # 解析绑定与触发
            if "绑定与触发" in line:
                golden_finger["binding"] = {
                    "desperate_binding": "绝境绑定：主角生死刺杀之夜强制激活，开局即高光，符合爽文第一集爆点逻辑。",
                    "core_essence": "核心本质：以画入道，画物成真、画技通神，将\"画画\"从文艺技能转化为玄幻杀伐+权谋操控的顶级能力。"
                }
            
            # 解析核心能力
            elif "核心能力" in line:
                golden_finger["abilities"] = {
                    "combat": "杀伐类：以画凝剑、凝修罗剑意、凝神兵、凝杀阵/结界，可瞬杀刺客、硬刚叛军、镇压魔神。",
                    "strategy": "权谋类：绘国运图、操控气运、看破伪装、解除血咒，以画作干预朝堂、天下格局。",
                    "support": "辅助类：引天地异象、刷摆烂值、加持众生信仰，为自身/势力/王朝赋能。"
                }
            
            # 解析奖励与升级体系
            elif "奖励与升级体系" in line:
                golden_finger["upgrade"] = {
                    "lottery": "抽奖机制：新手礼包→首次抽六剑奴→封并肩王解锁高级抽奖→至尊抽奖得白泽神兽蛋，摆烂值/剧情成就可兑换抽奖机会。",
                    "evolution": "能力进化：画道通神 → 解锁酒道通神 → 大道圣体 → 画道成神 → 仙帝级。",
                    "items": "道具迭代：苍生笔→进化版、乾坤画轴雏形→完整形态，战力持续飙升。",
                    "tasks": "任务体系：限时任务、国运任务、仙道飞升任务，完成即解锁势力/功法/神兽。"
                }
            
            # 解析专属资源：摆烂值
            elif "专属资源：摆烂值" in line:
                golden_finger["slacker_value"] = {
                    "acquisition": "获取方式：装废柴、流连风月、画美人、创立胭脂榜，摆烂越真，资源越多。",
                    "function": "核心作用：兑换抽奖、解锁能力，是主角\"扮废柴\"的核心动力。"
                }
        
        return golden_finger
    
    def parse_worldview(self, content):
        """
        解析世界观设定
        
        Args:
            content (str): 世界观文本内容
            
        Returns:
            dict: 世界观设定
        """
        worldview = {}
        lines = content.split('\n')
        
        for line in lines:
            line = line.strip()
            
            # 解析时空与版图
            if "时空与版图" in line:
                worldview["spacetime"] = {
                    "bottom": "底层：大奉皇朝（起点舞台）。",
                    "middle": "中层：东土、北荒、南林、西沼四大疆域，涵盖大明、炎夏、楼兰、北凛等百朝诸国。",
                    "top": "顶层：凡俗界→上古暗黑魔神界→仙界，格局从朝堂升维到三界。"
                }
            
            # 解析势力层级
            elif "势力层级（立体闭环）" in line:
                worldview["forces"] = {
                    "court": "朝堂：大奉皇室、镇北王府（军方顶流）、文武百官、禁军。",
                    "dark": "暗势力：百晓堂（情报）、七杀楼（杀手）、圣火教（北荒）、幽阁/黑莲教（魔神麾下）。",
                    "foreign": "域外：兽化人、蛮族、诸国联军、海外异族。",
                    "ultimate": "终极：上古暗黑魔神、仙界众仙。"
                }
            
            # 解析力量体系
            elif "力量体系" in line:
                worldview["power_system"] = {
                    "mortal": "凡俗：武道、兵权、权谋、商权、情报权。",
                    "fantasy": "玄幻：画道（主角专属）、修罗剑意、暗黑血咒、气运之力、众生信仰。",
                    "special": "特殊：神兽（白泽）、合体剑阵、国运画道大阵。"
                }
            
            # 解析核心规则
            elif "核心规则" in line:
                worldview["core_rules"] = "画作=国运载体，绘百朝一统、天下太平可引天地气运、众生信仰，气运决定王朝兴衰与个人战力；暗黑魔神以血咒、残魂毁灭世界，是底层终极威胁。"
        
        return worldview
    
    def parse_protagonist(self, content):
        """
        解析主角人设
        
        Args:
            content (str): 主角人设文本内容
            
        Returns:
            dict: 主角人设
        """
        protagonist = {}
        lines = content.split('\n')
        
        for line in lines:
            line = line.strip()
            
            # 解析双层人设
            if "双层人设（扮猪吃虎核心）" in line:
                protagonist["double_persona"] = {
                    "surface": "表层伪装：镇北王世子、摆烂废柴、纨绔画师，流连满春楼、醉心画美人，胸无大志、疯癫随性，让所有对手放松警惕。",
                    "core": "内核真身：穿越者，心思缜密、杀伐果断、权谋无双、护姐狂魔，心怀苍生，低调布局，不恋权位只图自在。"
                }
            
            # 解析核心标签
            elif "核心标签" in line:
                protagonist["core_tags"] = "摆烂画师、画道通神、护姐狂魔、一字并肩王、画道帝君、摆烂仙帝。"
            
            # 解析行为逻辑
            elif "行为逻辑" in line:
                protagonist["behavior_logic"] = "摆烂伪装→画道开挂→情报操盘→护姐夺权→一统百朝→灭魔救世→归隐飞升，全程扮废柴，躺赢成无敌。"
            
            # 解析核心羁绊
            elif "核心羁绊" in line:
                protagonist["core_bonds"] = "二姐陆长乐（辅佐成女帝，亲情向核心）、白泽（神兽伙伴）、六剑奴（死忠护卫）、陈蒹葭（徒弟+胭脂榜执掌）。"
        
        return protagonist
    
    def parse_core_conflicts(self, content):
        """
        解析核心冲突
        
        Args:
            content (str): 核心冲突文本内容
            
        Returns:
            list: 核心冲突列表
        """
        core_conflicts = []
        lines = content.split('\n')
        
        for line in lines:
            line = line.strip()
            
            # 解析七阶段核心冲突
            if "朝堂生存战（1-10集）" in line:
                core_conflicts.append({
                    "stage": 1,
                    "name": "朝堂生存战",
                    "episodes": "1-10集",
                    "description": "主角vs太子+皇后+外戚，核心：保命、护姐、夺权。"
                })
            elif "东土统一战（11-20集）" in line:
                core_conflicts.append({
                    "stage": 2,
                    "name": "东土统一战",
                    "episodes": "11-20集",
                    "description": "主角vs太子残党+大明+暗黑势力，核心：整合势力、平定东土。"
                })
            elif "北荒边患战（21-30集）" in line:
                core_conflicts.append({
                    "stage": 3,
                    "name": "北荒边患战",
                    "episodes": "21-30集",
                    "description": "主角vs兽化人+蛮族+暗黑血咒，核心：解除诅咒、收复北荒。"
                })
            elif "百朝争霸战（31-40集）" in line:
                core_conflicts.append({
                    "stage": 4,
                    "name": "百朝争霸战",
                    "episodes": "31-40集",
                    "description": "主角vs南林/西沼/大明联军，核心：一统天下版图。"
                })
            elif "盛世肃清战（41-50集）" in line:
                core_conflicts.append({
                    "stage": 5,
                    "name": "盛世肃清战",
                    "episodes": "41-50集",
                    "description": "主角vs魔神残魂+叛乱势力，核心：守护太平、清除内患。"
                })
            elif "神魔终极战（51-60集）" in line:
                core_conflicts.append({
                    "stage": 6,
                    "name": "神魔终极战",
                    "episodes": "51-60集",
                    "description": "主角vs上古暗黑魔神，核心：世界存亡、三界安危。"
                })
            elif "本心抉择战（61-70集）" in line:
                core_conflicts.append({
                    "stage": 7,
                    "name": "本心抉择战",
                    "episodes": "61-70集",
                    "description": "主角vs权位束缚，核心：拒绝仙帝之位，坚守摆烂初心。"
                })
        
        return core_conflicts
    
    def parse_differentiation(self, content):
        """
        解析新颖差异化设定
        
        Args:
            content (str): 新颖差异化设定文本内容
            
        Returns:
            list: 新颖差异化设定列表
        """
        differentiation = []
        lines = content.split('\n')
        
        for line in lines:
            line = line.strip()
            
            # 解析差异化设定
            if "画道+权谋+摆烂三重破圈" in line:
                differentiation.append({
                    "id": 1,
                    "name": "画道+权谋+摆烂三重破圈",
                    "description": "区别于普通武道爽文，以\"画画\"为核心金手指，画美人=赚资源，绘国运=定天下，文艺能力变杀伐利器，反差感极致。"
                })
            elif "摆烂人设反套路" in line:
                differentiation.append({
                    "id": 2,
                    "name": "摆烂人设反套路",
                    "description": "主角不张扬龙傲天，全程装废柴纨绔，表面醉卧美人画胭脂，暗中操盘天下，摆烂是手段，躺赢是结果，戳中当下受众偏好。"
                })
            elif "护姐+女帝养成主线" in line:
                differentiation.append({
                    "id": 3,
                    "name": "护姐+女帝养成主线",
                    "description": "核心动机为守护二姐，辅佐女性登顶女帝，非种马后宫，亲情向+大女主辅线，受众覆盖更广。"
                })
            elif "胭脂榜+百朝美人IP" in line:
                differentiation.append({
                    "id": 4,
                    "name": "胭脂榜+百朝美人IP",
                    "description": "画百朝皇后/美人入《胭脂评》，创立胭脂榜，既赚摆烂值，又搭情报网，颜值+剧情+爽点三合一，适配漫剧视觉呈现。"
                })
            elif "国运画道升维设定" in line:
                differentiation.append({
                    "id": 5,
                    "name": "国运画道升维设定",
                    "description": "个人画道与天下国运绑定，画作成天地气运核心，格局从朝堂权谋升维到世界救世，逼格拉满。"
                })
            elif "立体势力养成" in line:
                differentiation.append({
                    "id": 6,
                    "name": "立体势力养成",
                    "description": "六剑奴+百晓堂+七杀楼+大雪龙骑+白泽，护卫、情报、杀手、军队、神兽全覆盖，爽点密集不重复。"
                })
            elif "人设闭环大结局" in line:
                differentiation.append({
                    "id": 7,
                    "name": "人设闭环大结局",
                    "description": "从人间摆烂世子到仙界摆烂仙帝，全程贯彻\"摆烂\"核心，拒绝权位束缚，记忆点极强。"
                })
        
        return differentiation
    
    def parse_pleasure_logic(self, content):
        """
        解析核心爽点逻辑
        
        Args:
            content (str): 核心爽点逻辑文本内容
            
        Returns:
            list: 核心爽点逻辑列表
        """
        pleasure_logic = []
        lines = content.split('\n')
        
        for line in lines:
            line = line.strip()
            
            # 解析爽点逻辑
            if "开局绝境反杀，第一集即爆爽" in line:
                pleasure_logic.append("开局绝境反杀，第一集即爆爽")
            elif "扮猪吃虎密集打脸，反派全程被碾压" in line:
                pleasure_logic.append("扮猪吃虎密集打脸，反派全程被碾压")
            elif "势力/能力层层解锁，每集有小爽点，每阶段有大高潮" in line:
                pleasure_logic.append("势力/能力层层解锁，每集有小爽点，每阶段有大高潮")
            elif "护姐名场面+画道视觉异象，情绪与画面双适配" in line:
                pleasure_logic.append("护姐名场面+画道视觉异象，情绪与画面双适配")
            elif "阶段式胜利闭环，从废后到灭魔，爽点持续不断层" in line:
                pleasure_logic.append("阶段式胜利闭环，从废后到灭魔，爽点持续不断层")
        
        return pleasure_logic
