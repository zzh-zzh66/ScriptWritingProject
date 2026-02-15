# 第一集剧本生成器
# 负责生成第一集剧本，需要交代世界观、背景、势力层级、人物身份和金手指

from utils.color_marker import ColorMarker
from utils.sound_generator import SoundGenerator
from utils.writing_techniques import WritingTechniques
from utils.description_optimizer import DescriptionOptimizer

class FirstEpisodeGenerator:
    """
    第一集剧本生成器
    
    负责生成第一集剧本，需要特殊处理，交代世界观、背景、势力层级、人物身份和金手指
    """
    
    def __init__(self, config_manager, data_manager):
        """
        初始化第一集生成器
        
        Args:
            config_manager (ConfigManager): 配置管理器
            data_manager (DataManager): 数据管理器
        """
        self.config_manager = config_manager
        self.data_manager = data_manager
        self.color_marker = ColorMarker()
        self.sound_generator = SoundGenerator()
        self.writing_techniques = WritingTechniques()
        self.description_optimizer = DescriptionOptimizer()
    
    def generate(self, episode, outline):
        """
        生成第一集剧本
        
        Args:
            episode (int): 集数
            outline (dict): 剧情大纲
            
        Returns:
            str: 生成的剧本内容
        """
        script_content = self.build_script_structure(episode, outline)
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
        title = outline["title"]
        characters = "陆念离、陆长乐、七杀楼刺客首领、七杀楼刺客（两名）、镇北军士兵（数名）"
        scenes = "1-1 夜 外 大奉北域成安郡；1-2 夜 外 镇北王府·生辰宴；1-3 夜 内 镇北王府·世子寝殿"
        scene_content = self.generate_scene_content(outline)
        
        script = f"{title}\n\n"
        script += f"出场人物：{characters}\n\n"
        script += f"场景列表：{scenes}\n\n"
        script += scene_content
        
        return script
    
    def generate_scene_content(self, outline):
        """
        生成场景内容
        
        Args:
            outline (dict): 剧情大纲
            
        Returns:
            str: 场景内容
        """
        content = ""
        content += self.generate_opening_world_view()
        content += self.generate_banquet_end_scene()
        content += self.generate_bedroom_enter_scene()
        content += self.generate_danger_scene()
        content += self.generate_sister_arrival_scene()
        content += self.generate_ending_hook()
        return content
    
    def generate_opening_world_view(self):
        """
        生成开场世界观全景介绍场景
        
        Returns:
            str: 开场场景内容
        """
        content = "1-1 夜 外 大奉北域成安郡\n\n"
        
        content += "△金色字体，横向，悬浮在场景上方，显示：俗世百朝\n"
        content += "△俯视图：俗世百朝东南西北四方地图，武道兴盛，朝堂江湖危机四伏\n"
        content += "旁白：这是俗世百朝，一个架空玄幻世界，武道兴盛，朝堂江湖危机四伏。\n"
        content += "△金色字体，横向，悬浮在场景上方，显示：大奉皇朝\n"
        content += "△俯视图：大奉皇朝，镇北王府在北，皇宫在南\n"
        content += "旁白：大奉皇朝，镇北王府镇守北域，皇室忌惮兵权。今日镇北王府世子陆念离二十岁生辰，太子党派七杀楼刺客前来刺杀。\n"
        
        return content
    
    def generate_banquet_end_scene(self):
        """
        生成生辰宴散场场景
        
        Returns:
            str: 生辰宴散场场景内容
        """
        content = "\n1-2 夜 外 镇北王府·生辰宴\n\n"
        
        content += "△金色字体，横向，悬浮在场景上方，显示：镇北王府·生辰宴\n"
        content += "△夜，镇北王府·生辰宴，烛火通明，宾客尽欢，酒杯碰撞声此起彼伏。\n"
        
        content += "△陆长乐站在宴席旁，穿黑色劲装，腰间佩剑，眉头微皱。\n"
        content += "△金色字体，竖向，悬浮在陆长乐旁边，显示：陆长乐：镇北王长女，镇北军统领\n"
        
        content += "△陆念离装醉，脚步踉跄，向陆长乐告别。\n"
        content += "陆念离（脚步踉跄，挥手）：今天我庆生辰，大家吃好喝好！\n"
        content += "△陆长乐站在陆念离身边，眉头微皱，扶住陆念离。\n"
        content += "陆长乐（扶住陆念离）：你少喝点，今天别出什么事。\n"
        content += "陆念离（OS）：二姐，没事，今晚过了就好。\n"
        
        return content
    
    def generate_bedroom_enter_scene(self):
        """
        生成进入寝殿场景
        
        Returns:
            str: 进入寝殿场景内容
        """
        content = "\n1-3 夜 内 镇北王府·世子寝殿\n\n"
        
        content += "△金色字体，横向，悬浮在场景上方，显示：镇北王府·世子寝殿\n"
        content += "△夜，镇北王府世子寝殿，烛火摇晃，桌案摊半幅美人图，狼毫笔斜插墨砚。\n"
        content += "△陆念离走进寝殿，走到床前。\n"
        content += "△陆念离突然清醒，眼中精光一闪。\n"
        content += "△陆念离侧躺，左臂压枕，右腿微屈，腰间玉画筒斜抵床沿，筒身雕纹反光。\n"
        content += "陆念离（OS）：五年前穿越成了镇北王世子陆念离，摆烂到现在终于完成了初始任务，解锁了摆烂系统。今晚过了，就可以激活系统了。\n"
        
        return content
    
    def generate_danger_scene(self):
        """
        生成遭遇生死危机场景
        
        Returns:
            str: 遭遇生死危机场景内容
        """
        content = ""
        
        content += "△三道黑影从后窗翻身入，足尖垫黑布落地，反握寒刃围向床榻。\n"
        
        content += "△为首黑影穿夜行衣，蒙面，手持寒刃。\n"
        content += "△金色字体，竖向，悬浮在为首黑影旁边，显示：七杀楼刺客首领：太子雇佣的杀手\n"
        
        content += "七杀楼刺客首领（抬右手，食指指陆念离）：太子有令，陆念离首级留下！留痕迹，咱们都别活！\n"
        
        content += self.color_marker.mark_yellow("△七杀楼刺客首领挥刀劈陆念离眉心，寒光擦鼻尖过。\n")
        content += "△锦缎被劈出裂口。\n"
        content += "△刀距眉心两寸时，陆念离睁眼。\n"
        content += "△陆念离左手撑床翻身，右腿屈膝踹向刺客首领小腹。\n"
        content += "陆念离（踹中刺客）：朱峰派你们来送死！\n"
        content += "△翻身时月白寝衣被划开长口，后背渗血珠顺脊椎滑。\n"
        content += "△陆念离滚到床沿，指尖勾住玉画筒，指节泛白。\n"
        
        content += self.color_marker.mark_green("△半空中浮现淡蓝色透明面板，上面显示\"系统绑定成功！新手大礼包激活：苍生笔、修罗剑意！\"\n")
        content += "声音提示：叮（系统提示音）\n"
        content += "系统：系统绑定成功！新手大礼包激活：苍生笔、修罗剑意！\n"
        
        content += self.color_marker.mark_green("△系统面板：半空中浮现淡蓝色透明面板，上面写着\"新手任务·摆烂反杀：10分钟击杀三名七杀楼刺客，奖励摆烂值1000点+首次抽奖权限！超时解绑！\"\n")
        content += "声音提示：叮（系统提示音）\n"
        content += "系统：新手任务已发布！\n"
        
        content += "△陆念离周身冒淡金光，后背伤口快速结痂。\n"
        content += "△掌心现半透明苍生笔虚影，笔杆刻\"画通万物\"四字。\n"
        content += "△他甩胳膊，笔尖指向刺客首领。\n"
        content += "陆念离（看向刺客首领）：藏头露尾的东西，也配叫顶尖刺客？\n"
        
        content += self.color_marker.mark_yellow("△苍生笔虚影点出，金色画纹变三寸剑气。\n")
        content += "△剑气穿透刺客首领黑衣，从后心穿出。\n"
        content += "△刺客首领瞳孔放大，直挺挺倒地。\n"
        content += self.sound_generator.generate_sound("当啷", "寒刃落地声")
        
        content += "剩余两名刺客（左右分开，挥刀扑来）：这小子藏了实力！用合击术！\n"
        
        content += "△两刺客一人攻下盘，一人劈肩头，刀刃带风刮动衣摆。\n"
        content += "△陆念离脚尖点地跳半尺。\n"
        content += "△苍生笔连点两下，金色画纹变锁链。\n"
        content += "△锁链一端缠左侧刺客手腕，一端勒右侧刺客脖子。\n"
        content += "陆念离（收劲）：不堪一击。\n"
        content += "△陆念离手腕收劲，锁链绷紧。\n"
        content += "△两声脆响，两刺客脖子折断，尸体堆在首领旁。\n"
        content += self.sound_generator.generate_sound("咔嚓", "骨头断裂声")
        content += "△血在青砖上漫开。\n"
        
        content += self.color_marker.mark_green("△系统面板：半空中浮现淡蓝色透明面板，上面写着\"任务完成（耗时3分27秒）！摆烂值1000点到账！首次抽奖权限解锁，是否立即抽奖？\"\n")
        content += "声音提示：叮（系统提示音）\n"
        content += "系统：任务完成！摆烂值1000点到账！\n"
        
        content += "△陆念离收了苍生笔和金光，后背伤口完全愈合。\n"
        content += "△指尖点系统面板\"立即抽奖\"，轮盘飞速转动。\n"
        content += "△轮盘停在\"六剑奴召唤权限\"。\n"
        content += "△六道黑影凭空现，单膝跪地，戴青铜面具，剑插地面。\n"
        content += "△金色字体，竖向，悬浮在六道黑影旁边，显示：六剑奴：系统新手礼包势力\n"
        content += "六剑奴（齐声）：属下六剑奴，参见主人！愿誓死效忠！\n"
        
        content += self.color_marker.mark_green("△系统面板：半空中浮现淡蓝色透明面板，上面写着\"抽中六剑奴召唤权限（冷却24小时），可随时召唤执行任务！\"\n")
        content += "声音提示：叮（系统提示音）\n"
        content += "系统：六剑奴召唤权限已解锁！\n"
        
        return content
    
    def generate_sister_arrival_scene(self):
        """
        生成陆长乐赶到场景
        
        Returns:
            str: 陆长乐赶到场景内容
        """
        content = ""
        
        content += "△殿门\"吱呀\"开，陆长乐率镇北军冲进来。\n"
        content += self.sound_generator.generate_sound("吱呀", "门打开声")
        content += "△陆长乐看到三具刺客尸体和陆念离。\n"
        content += "陆长乐（看向刺客尸体，看向陆念离）：谁敢动我弟弟！\n"
        content += "陆念离（看向陆长乐）：二姐，我没事。太子派来的刺客，已经被我杀了。\n"
        content += "陆长乐（握住陆念离的手）：没事就好。太子敢动你，我定要他付出代价！\n"
        
        return content
    
    def generate_ending_hook(self):
        """
        生成结尾钩子
        
        Returns:
            str: 结尾钩子内容
        """
        content = ""
        
        content += "△陆念离看向刺客首领尸体，发现怀中掉落一枚刻有幽阁标记的令牌。\n"
        
        content += self.color_marker.mark_blue("△系统面板：半空中浮现淡蓝色透明面板，上面显示\"检测到暗黑血咒气息，危险等级：★★★\"\n")
        content += "声音提示：警告（系统提示音）\n"
        content += "系统：检测到暗黑血咒气息！危险等级：★★★！\n"
        
        content += self.color_marker.mark_green("△系统面板：半空中浮现淡蓝色透明面板，上面写着\"主线任务已激活：瓦解太子势力，护姐姐陆长乐登基女帝，一统百朝，终结乱世。当前进度：0/10（瓦解太子死忠势力）。奖励：解锁六剑奴召唤权限、百晓堂初级情报网。\"\n")
        content += "声音提示：叮（系统提示音）\n"
        content += "系统：主线任务已激活！\n"
        
        return content
