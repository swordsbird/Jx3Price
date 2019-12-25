item_weight = {}
item_weight['萝莉'] = {}
'''五红': 2,  '四红': 1.5,  '六红': 1.5, '一代金': 1.5, '狐金': 2, '狐狸毛': 1.5,
    '一代重阳盒': 1.5, '红彩云': 2, '珠盏映粉蕊': 1.5, '银月金虹': 1.5,
    '劲足赤兔': 1.5, '一代粉': 1.5, '100级橙武': 1.5,'黑金夜斩白': 1.5, '三山四海': 1.5, '粉白菜': 2,
    '蓝罗姆': 2, '一代黑': 1.5, '济世菩萨': 1.5, ' 三尺青锋': 1.5,
    '鸡盒': 1.5, '星河清梦': 1.5, '绿不欺': 1.5,
    '紫白菜': 1.5, '资历金': 1.5, '月伴晨星': 1.5,
    '济苍生': 1.5, '瘸腿赤兔': 1.5, '开明参虎': 1.5, '六翼': 1.5, '蓝彩云': 1.5, '大雕': 1.5, '白罗姆': 2, '业火封狼': 1.5
}'''
item_weight['成女'] = {
    '五红': 1.5,  '四红': 1.5,  '六红': 1.5, '一代金': 1.5, '狐金': 1.5, '狐狸毛': 1.5,
    '一代黄': 1.5, '一代重阳盒': 1.5, '蓝娃娃': 1.5,
    '橙繁': 1.5, '粉繁': 1.5, '一代元宵盒': 1.5, '红彩云': 1.5, '黑盒': 1.5,
    '珠盏映粉蕊': 1.5, '白娃娃': 1.5, '银月金虹': 1.5,
    '一代红': 1.5, '劲足赤兔': 1.5, '一代粉': 1.5, '100级橙武': 1.5, '黑风华': 1.5,
    '紫风华': 1.5, '一代白': 1.5, '黑金夜斩白': 1.5, '三山四海': 1.5, '粉白菜': 1.5,
    '二代黑': 1.5, '蓝罗姆': 1.5, '谷雨': 1.5, '一代黑': 1.5, '济世菩萨': 1.5, ' 三尺青锋': 1.5,
    '二代蓝': 1.5, '黑风露': 1.5, '鸡盒': 1.5, '星河清梦': 1.5, '绿不欺': 1.5,
    '紫白菜': 1.5, '资历金': 1.5, '焰归': 1.5, '一代紫': 1.5, '月伴晨星': 1.5,
    '济苍生': 1.5, '瘸腿赤兔': 1.5, '开明参虎': 1.5, '黑墨韵': 1.5, '六翼': 1.5, '一代白': 1.5,
    '白金夜斩白': 1.5, '蓝彩云': 1.5, '大雕': 1.5, '白罗姆': 1.5, '业火封狼': 1.5, '黑年轮': 1.5
}
item_weight['成男'] = {
    '四红': 1.5,  '六红': 1.5, '一代金': 1.5, '狐金': 1.5, '狐狸毛': 1.5,
    '一代黄': 1.5, '蓝娃娃': 1.5,
    '黑盒': 1.5,
    '珠盏映粉蕊': 1.5, '白娃娃': 1.5, '银月金虹': 1.5,
    '一代红': 1.5, '劲足赤兔': 1.5, '100级橙武': 1.5, '一代白': 1.5, '黑金夜斩白': 1.5, '三山四海': 1.5,
    '二代黑': 1.5, '一代黑': 1.5, '济世菩萨': 1.5, ' 三尺青锋': 1.5,
    '二代蓝': 1.5, '鸡盒': 1.5, '星河清梦': 1.5, '资历金': 1.5, '焰归': 1.5, '一代紫': 1.5, '月伴晨星': 1.5,
    '济苍生': 1.5, '瘸腿赤兔': 1.5, '开明参虎': 1.5, '一代白': 1.5,
    '白金夜斩白': 1.5, '大雕': 1.5, '业火封狼': 1.5, '黑年轮': 1.5
}
item_weight['正太'] = {}
body_penalty = {'正太': 0.7, '萝莉': 0.8, '成男': 1.3, '成女': 1.2}
random_change_weight = { '红发': 120, '金发': 120, '六限': 120, '限时': 140, '复刻': 140, '挂宠': 160, '盒子': 300 }

fix_pairs = [['红发', ['rhair']], ['金发', ['ghair']], ['五限', ['cl5']], ['六限', ['cl6']], [
    '限时', ['cl7']], ['复刻', ['cln']], ['挂宠', ['pat']], ['盒子', ['box', 'boxn']]]

addition_pairs = [['秃头', ['四红', '五红', '六红', '一代金', '狐金']]] #, ['有点秃头', ['四红', '五红', '六红', '一代金']]]
for x in item_weight:
    for p in addition_pairs:
        item_weight[x][p[0]] = 2

reserved_items = ['四红', '五红', '六红', '猴红', '羊红', '一代金', '狐金', '猴金', '龙女金', '中秋金', '狗金', '丝路金', '兔金', '考金', '粉繁',
                  '橙繁', '红墨韵', '黑墨韵', '黑风露', '蓝风露', '粉白菜', '紫白菜',
                  '谷雨', '情阅', '白金夜斩白', '黑金夜斩白', '白罗姆', '蓝罗姆', '黑风华', '红彩云', '蓝彩云', '蓝公主', '粉公主', '粉人面', '蓝人面',
                  '绿不欺', '蓝不欺', '白娃娃', '粉娃娃', '黄娃娃', '蓝娃娃', '黑年轮', '红年轮', '黄年轮',
                  '蓝年轮', '白无色',  '黄兰若', '红兰若', '黑兰若', '蓝兰若', '红容与', '绿容与', '紫容与',
                  '粉容与', '黄长安', '绿长安', '红长安', '紫长安', '粉兰亭', '紫兰亭', '黄兰亭', '白兰亭', '白九壤', '黄九壤', '粉九壤', '蓝九壤', '红长天', '绿长天', '蓝长天', '白长天',
                  '红舞步', '粉舞步', '蓝舞步', '黑舞步', '白重天', '粉重天', '黄重天', '黑重天', '蓝天涯', '紫天涯', '黑天涯', '绿天涯',
                  '飒西风陵烟', '飒西风雪回', '飒西风苍璧', '飒西风清江', '飒西风丹壑', '飒西风龙旌', '绿中宵', '黄中宵', '紫中宵', '白中宵',
                  '榆塞裂衿', '榆塞斩芒', '榆塞寒塘', '榆塞振锋', '黑榆塞', '榆塞落旌',
                  '打歌服', '明镜高悬', '富婆套', '复刻繁折风', '复刻繁故幽', '复刻绿白菜', '复刻瓜白菜', '复刻霜降', '复刻惊蛰', '黑夜斩白', '白夜斩白', '复刻粉罗姆',
                  '复刻蓝罗姆', '复刻红紧那', '复刻白策马', '复刻黑策马', '复刻黑彩云',
                  '复刻粉彩云', '复刻黑潇湘', '复刻白潇湘', '复刻蓝天河', '复刻黄天河', '金罗姆', '望月', '情人枕', '六周年龙', '孔雀', '六翼', '特效粉', '金鱼', '狐狸毛', '钰瓣', '天辉', '暗夜',
                  '喵萝干', '狄仁杰黑', '狄仁杰白', '一代黄', '一代白', '一代粉', '一代黑', '一代红', '一代紫', '二代粉',
                  '二代蓝', '二代白', '二代紫', '二代红', '二代黑', '狼头', '黑竹笋', '白莲花', '蓝扇子',
                  '秃盒', '鸡盒', '花盒', '红盒', '飞天盒', '丝路盒', '粉马盒', '黑马盒', '一代重阳盒', '一代七夕盒', '一代中秋蓝', '一代中秋粉', '一代元宵盒', '狄仁杰盒',  '熊猫', '大雕', '复刻',
                  '下架', '五限', '六限', '限时', '限量', '成衣', '奇遇', '红发', '金发', '白发', '黑发', '盒子', '挂宠', '披风', '五甲', '奇趣', '拓印', '脚印', '100小铁', '宠物', '资历']
