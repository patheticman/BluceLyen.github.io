#coding:utf-8
import re
import sys

reload(sys)
sys.setdefaultencoding('utf8')

def valid_jsontxt(content):
    if type(content) == type(u""):
        res = content.encode("utf-8")
    else:
        res = str(content)
    return res.replace('\n', "").replace("\r", "").replace('\001', "").replace("\u0001", "")


for line in sys.stdin:
    line if isinstance(line,unicode) else line.encode("utf-8")
    keywords = '朱士行|支娄迦谶|支遁|真可|净土五经|古尊宿语录|金刚决疑|大乘佛教|四大菩萨|唯识宗|三论宗|天台宗|华严宗|禅宗|净土宗|律宗|密宗|俱舍宗|莲花生|阿底峡|宗咯巴|松赞干布|尺尊公主|囤弥·桑布扎|文成公主|寂护大师|甘珠尔|大藏经（三藏经）|班禅|密宗|喇嘛教|吐蕃七觉士|宁玛派|萨迦派|噶举派|噶当派|桑耶寺|大昭寺|托林寺|布达拉宫|格鲁派主寺|天葬|土葬|水葬|塔葬|火葬|天主|教皇|牧首|正教 救世主|耶稣 摩西|YHWH|托拉（妥拉）|犹太法典|塔纳赫|摩西五经|摩西十戒|先知书|特选子民|伊玛目|伊斯玛仪|穆罕默德|古兰经|清真|伊斯兰|真主|安拉|胡达|伊玛尼|伊赫桑|作证言|清真言|主麻|主麻吉庆|塞俩目|色兰|回族|东乡族|保安族|塔吉克族|乌孜别克族|穆斯林|道教|真人|天师|无上天尊|佛诞节|浴佛节|藏历年|林卡节|雪顿节|望果节|燃灯节|驱鬼节|仙女节|朝山节|传昭大会|传昭小会|佛吉祥日|安息日|赎罪日|逾越节|七七节|帐棚节|光明节|主麻吉庆|古兰经|开斋节|宰牲节|圣纪|三清节|三元节|五腊日|王母圣诞|南华真经|心印经|道德真经|道教 萨拉斯瓦蒂节|蛇节|大壶节|排灯节|杜尔迦节|克里希纳神诞辰日|十胜节|提吉节|斋普尔大象节|除十节|大乘佛教|唯识宗|三论宗|天台宗|华严宗|禅宗|净土宗|律宗|密宗|俱舍宗 莲花生|阿底峡|宗咯巴|小乘佛教|南传大藏经|南传大般涅槃经|摩西|YHWH|托拉（妥拉）|犹太法典|塔纳赫|摩西五经|摩西十戒|先知书|特选子民 穆罕默德|古兰经|清真|伊斯兰|真主|安拉|胡达|伊玛尼|伊赫桑|作证言|清真言|主麻|主麻吉庆|塞俩目|色兰|回族|东乡族|保安族|塔吉克族|乌孜别克族|穆斯林|大梵天|提婆|大自在天|湿婆|妙毗天|毗湿奴|梨俱吠陀|摩诃婆罗多|薄迦梵歌|罗摩衍那|往世书|主神论|种姓分立|祭祀万能|吠陀经典|梵天|罗刹女|佛陀|释迦牟尼|菩提萨埵|阿罗汉|菩提心|阿弥陀佛|涅槃|达摩|僧伽|菩提树|娑罗树|圣客沙|法师|新约|圣经|教会|原罪|基督|主教|天主|东正|凡事谢恩|阿门|哈利路亚|圣餐|主日学|福音'
    match_words = ','.join(list(set(re.findall(keywords, line))))
    print match_words
