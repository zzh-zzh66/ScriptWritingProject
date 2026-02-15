# 正常集数剧本生成器
# 负责生成第三集及以后的剧本

from utils.color_marker import ColorMarker
from utils.sound_generator import SoundGenerator
from utils.scene_selector import SceneSelector
from utils.character_manager import CharacterManager

class NormalEpisodeGenerator:
    """
    正常集数剧本生成器
    
    负责生成第三集及以后的剧本
    """
    
    def __init__(self, config_manager, data_manager):
        """
        初始化正常集数生成器
        
        Args:
            config_manager (ConfigManager): 配置管理器
            data_manager (DataManager): 数据管理器
        """
        self.config_manager = config_manager
        self.data_manager = data_manager
        self.color_marker = ColorMarker()
        self.sound_generator = SoundGenerator()
        self.scene_selector = SceneSelector(data_manager)
        self.character_manager = CharacterManager(data_manager)
    
    def generate(self, episode):
        """
        生成正常集数剧本
        
        Args:
            episode (int): 集数
            
        Returns:
            str: 生成的剧本内容
        """
        # 构建剧本结构
        script_content = self.build_script_structure(episode)
        return script_content
    
    def build_script_structure(self, episode):
        """
        构建剧本结构
        
        Args:
            episode (int): 集数
            
        Returns:
            str: 剧本内容
        """
        # 标题
        title = f"第{episode}集：满春楼"
        
        # 出场人物
        characters = "陆念离、陈蒹葭（满春楼头牌）、百晓通、六剑奴、达官贵人（数名，京城权贵）"
        
        # 场景列表
        scenes = "3-1 夜 内 长安·满春楼大厅；3-2 夜 内 长安·满春楼顶层雅间"
        
        # 场景内容
        scene_content = self.generate_scene_content()
        
        # 组合剧本
        script = f"{title}\n\n"
        script += f"出场人物：{characters}\n\n"
        script += f"场景列表：{scenes}\n\n"
        script += scene_content
        
        return script
    
    def generate_scene_content(self):
        """
        生成场景内容
        
        Returns:
            str: 场景内容
        """
        content = ""
        
        # 场景1：满春楼大厅
        content += "3-1 夜 内 长安·满春楼大厅\n\n"
        
        # 环境描写
        content += "△满春楼大厅挂几十盏琉璃灯，灯光亮如白昼。中央舞池里，舞姬穿彩衣跳舞，水袖甩起时带起风，丝竹声、笑声、酒杯碰撞声混在一起。达官贵人坐满桌椅，有的搂歌姬喝酒，有的凑一起说话。\n"
        
        # 陆念离在二楼
        content += "△二楼临窗软榻，陆念离斜躺，左手搭在榻沿，右手端着清酒杯。小桌上摆着宣纸、墨砚，狼毫笔放在宣纸上未动。六剑奴隐在软榻两侧阴影里。百晓通站在软榻后，弯腰贴陆念离耳朵说话。\n"
        
        # 百晓通汇报
        content += "百晓通（声音压得极低）：主人，楼下穿紫袍的是工部侍郎李嵩，上周给太子送了五万两；穿绿袍的是光禄寺卿王凯，帮太子管宫外产业。太子最近常和国舅赵成见面，密谈内容还在查。\n"
        
        # 陆念离回应
        content += "陆念离（喝了口酒）：不急，慢慢查。听说满春楼头牌陈蒹葭会抚琴，看看她的才情。\n"
        
        # 陈蒹葭出场
        content += "△丝竹声突然停，高台上传来古琴声。陈蒹葭从后台走出，穿月白色纱裙，裙摆绣浅淡芦花，怀抱古琴走到台前坐下。她未施粉黛，眉眼温婉，指尖拨弦，轻声唱江南小调，声音柔缓。大厅瞬间安静，达官贵人们都看向高台。\n"
        
        # 达官贵人议论
        content += "达官贵人甲（端着酒杯，侧身对旁边人说）：陈姑娘这气质，真是绝了！可惜没画师能画出来。\n"
        content += "达官贵人乙（叹气，摇头）：上次王画师画她，跟普通歌姬没两样。谁能画她神韵，我出一万两买画！\n"
        
        # 陆念离决定
        content += "△陆念离嘴角勾了勾，抬手示意百晓通。\n"
        content += "陆念离（声音不大，刚好传到百晓通耳中）：去请陈姑娘，到顶层雅间。说我要给她画画。\n"
        
        # 场景2：满春楼顶层雅间
        content += "\n3-2 夜 内 长安·满春楼顶层雅间\n\n"
        
        # 环境描写
        content += "△顶层雅间开着窗，能看到长安夜景。房间中央摆红木画案，上铺白色宣纸，旁边放徽墨、湖笔、端砚。烛火放在画案一侧，光线柔和，照亮宣纸。陈蒹葭坐在画案对面椅子上，双手放在膝盖上，身体微前倾，显拘谨。\n"
        
        # 陈蒹葭行礼
        content += "陈蒹葭（起身敛衽躬身）：小女陈蒹葭，见过世子殿下。不知殿下要为小女画什么？\n"
        
        # 陆念离回应
        content += "陆念离（抬手让她坐下，自己走到画案前拿起湖笔）：不用多礼。你气质如蒹葭，便画《蒹葭苍苍》。\n"
        
        # 陆念离作画
        content += "△陆念离收敛慵懒，看向宣纸。他召出苍生笔虚影，与手中湖笔重叠，笔尖蘸徽墨，轻轻落在宣纸上。画道之力从笔尖流出，墨色在宣纸上晕开，快速勾勒出陈蒹葭的眉眼、纱裙上的芦花，线条细腻。\n"
        
        # 画成引异象
        content += "△最后一笔落下，窗外突然飘起漫天芦花，金色霞光从云层透出，照得芦花发亮。满春楼楼下传来一片惊呼声，有人推开窗户抬头看。\n"
        
        # 声音提示
        content += self.sound_generator.generate_sound("哇！", "惊呼声")
        
        # 系统提示（绿色标记）
        content += self.color_marker.mark_green("系统提示：【叮！创作《蒹葭苍苍》评级神品！引天地异象（漫天芦花+金色霞光）！奖励摆烂值3000点！画道通神熟练度+200，解锁新能力\"画中藏物\"！】\n")
        
        # 陈蒹葭反应
        content += "△陈蒹葭快步走到画案前，盯着宣纸上的画，眼睛慢慢红了，眼泪顺着脸颊滑落。她突然转身，\"扑通\"跪在陆念离面前。\n"
        content += self.sound_generator.generate_sound("扑通", "跪地声")
        
        # 陈蒹葭请求
        content += "陈蒹葭（声音哽咽）：殿下画技出神入化！求殿下收小女为徒！小女愿侍奉殿下左右，潜心学画！\n"
        
        # 陆念离回应
        content += "陆念离（弯腰扶她起身，指尖擦去她脸颊的眼泪）：我收你为徒。但你要帮我——留意满春楼达官贵人的谈话，记下太子死忠的动向，每三天让百晓通来取情报。\n"
        
        # 陈蒹葭回应
        content += "陈蒹葭（用力点头）：弟子遵令！定不辱使命！\n"
        
        # 陆念离赠画
        content += "△陆念离拿起画卷，轻轻卷好递到陈蒹葭手中。他走到窗边，看着楼下热闹的景象，指尖捏着窗沿。\n"
        content += "陆念离（语气冷）：有了满春楼的情报，朱峰，我看你往哪逃。\n"
        
        # 系统提示（绿色标记）
        content += self.color_marker.mark_green("系统提示：【主线任务进度更新：2/10（瓦解太子死忠势力）。下一步：揭露太子勾结外敌罪证，在朝堂上瓦解太子势力。】\n")
        
        # 太子眼线离开
        content += "△楼下人群里，一个穿灰袍的人转身就走，六剑奴刚要动，被陆念离抬手拦住。\n"
        content += "陆念离（嘴角勾笑）：让他走，正好给太子报信。\n"
        
        return content
