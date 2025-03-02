import streamlit as st
import numpy as np
import random as rnd
import matplotlib as mpl
import matplotlib.pyplot as plt
from datetime import datetime as dt
import time
import datetime

mpl.rcParams["font.sans-serif"] = ["SimHei"]  # 保证显示中文字
mpl.rcParams["axes.unicode_minus"] = False  # 保证负号显示
mpl.rcParams["font.size"] = 18  # 设置字体大小
mpl.rcParams["ytick.right"] = True
mpl.rcParams["xtick.top"] = True
mpl.rcParams["xtick.direction"] = "in"  # 坐标轴上的短线朝内，默认朝外
mpl.rcParams["ytick.direction"] = "in"
global h, interval, m, s, h_s
# https://gzlgfang-st-apps/EEtest-st-spp
# streamlit  run "g:/st-app/st_EEtest.py"
# 基层生态环工作人员知识学习考试系统
# 包含隐患排查与治理、法律法规、各类标准、信访回复、噪声检测与争议、水质检测与争议、废气检测与争议、土壤检测
# 单选题 str_test[序号] = ["下面有关一字的四个词组，哪个不是成语:", '一成不变', '一个不剩', '一夫当关', '一蹴而就']
# start_time = dt.now()
# start_time = time.time()
start_time = time.process_time()
answer = 600 * [1 * ["NA"]]
str_test = 600 * [6 * ["NA"]]
# str_test = list()
# 隐患排查与治理：0-99，共100题
str_test[0] = ["企业环境安全隐患排查的时间为", "制定环境应急预案前", "制定环境应急预案中", "环境应急预案报备后", "任何时候", 3]
str_test[1] = [
    "企业突发环境事件风险分级方法》中风险评估分析的M值是指",
    "风险物质数量与临界量比值",
    "突发环境事件风险物质临界量",
    "生产工艺过程与环境风险控制水平",
    "环境风险受体敏感程度",
    3,
]
str_test[2] = [
    "《突发环境事件应急管理办法》第三十八条规定未按规定开展环境安全隐患排查治理工作的可以处",
    "一万元以上二万元以下罚款",
    "一万元以上三万元以下罚款",
    "二万元以上三万元以下罚款",
    "三万元以上五万元以下罚款",
    2,
]
str_test[3] = [
    "企业对待环境安全隐患和风险的态度是",
    "发现隐患必须及时处理，而必要的风险允许存在",
    "发现隐患和风险都必须及时处理",
    "发现风险必须及时处理，而一般隐患允许存在",
    "发现隐患和风险都不必及时处理",
    1,
]
str_test[4] = [
    "环境安全隐患资料中常说的“一案三制”是指",
    "消防预案、体制、机制、法制",
    "突发环境事件应急预案、体制、机制、规制",
    "安全预案、体制、机制、法制",
    "突发环境事件应急预案、体制、机制、法制",
    4,
]
str_test[5] = ["《中华人民共和国环境保护法》（第一版）通过的时间为", "1986年", "1989年", "2004年", "2005年", 2]
str_test[6] = ["水质检测中有一项指标简称SS,它的含义是", "水中化学耗氧量", "水中生物耗氧量", "水中悬浮固体含量", "水中细菌含量", 3]
str_test[7] = ["广东省环境保护条例是哪一年通过的", "1998年", "2004年", "1996年", "2008", 2]
str_test[8] = ["下面哪种物质不属于危险化学品", "84消毒液", "甲醇", "食用油", "乙醇", 3]
str_test[9] = ["下面那一种不属于企业隐患排查方式", "综合排查", "全厂排查 ", "日常排查", "抽查", 2]
str_test[10] = ["下面哪一种属于环境安全隐患一般分类方法中的一类", "特大隐患", "重大隐患", "较大隐患", "常规隐患", 2]
str_test[11] = ["《中华人民共和国环境保护法》第一次修订版实施时间为", "1989年", "2004年", "2005年", "2015年", 4]
str_test[12] = ["中华人民共和国生态环境部成立于哪一年？", "1990", "1998", "2018", "2019", 3]
str_test[13] = ["大气中细微颗粒物又称PM2.5，其中2.5对应的单位为", "毫米", "微米", "纳米", "厘米", 2]
str_test[14] = ["废水指标中的BOD是指", "化学需氧量", "物理需氧量", "生化需氧量", "生物需氧量", 4]
str_test[15] = ["大气中的VOCs是指", "悬浮颗粒物", "扬尘", "挥发性有机物", "氮气", 3]
str_test[16] = [
    "挥发性有机物无组织排放标准的实施时间为",
    "2019年5月4日",
    "2018年5月4日",
    "2020年7月1日",
    "2019年7月1日",
    4,
]
str_test[17] = ["《中华人民共和国噪声污染防治法》开始施行年份为", "1996", "1997", "2018", "2022", 4]
answer[0:18:1] = [3, 3, 2, 1, 4, 2, 3, 2, 3, 2, 2, 4, 3, 2, 4, 3, 4, 4]

##100-199
##环境保护法试题
str_test[100] = ["2015年1月1日起实施的《中华人民共和国环境保护法》共有多少章？", "5章", "1章", "7章", "8章", 3]
str_test[101] = [
    "2015年实施的《中华人民共和国环境保护法》的目的是",
    "保护环境",
    "促进经济和社会发展",
    "提高人民生活质量",
    "保护和改善生活环境与生态环境",
    4,
]
str_test[102] = [
    "《中华人民共和国环境保护法》适用于中华人民共和国领域和中华人民共和国管辖的（  ）。",
    "其他岛屿",
    "其他海域",
    "其他领空",
    "其他大陆架",
    2,
]
str_test[103] = ["每年的什么时候为环境日？", "5月6日", "6月5日", "9月5日", "10月28日", 2]
str_test[104] = [
    "2024年中国环境日的主题是什么？",
    "全面推进青山绿水建设",
    "全面推进美丽乡村建设",
    "全面推进美丽神州建设",
    "全面推进美丽中国建设",
    4,
]
str_test[105] = [
    "下面描述正确的是",
    "保护环境是国家的基本国策",
    "保护环境是国家的根本国策",
    "保护环境是国家的重要国策",
    "保护环境是国家的顶层国策",
    1,
]
str_test[106] = [
    "下面哪一条不是环境保护原则",
    "环境保护坚持保护优先、预防为主、综合治理原则",
    "公众参与原则",
    "损害担责的原则",
    "经济社会发展与环境保护相协调原则",
    4,
]
str_test[107] = [
    "某企业违法排放污染物，受到罚款处罚，被责令改正，但拒不改正的，依法作出处罚决定的行政机关可以自责令改正之日的次日起，按照原处罚数额",
    "加倍处罚",
    "三倍处罚",
    "按日连续处罚",
    "原样处罚",
    3,
]
str_test[108] = [
    "已建成企业其污染物排放超过标准的，县级以上人民政府环境保护主管部门可以责令其采取",
    "限期拆除",
    "停产整治",
    "限期治理",
    "上报处罚",
    2,
]
str_test[109] = [
    "下面描述不正确的是",
    "环境保护规划的内容应当与土地利用总体规划相衔接",
    "环境保护规划的内容应当与科学技术发展规划相衔接",
    "环境保护规划的内容应当与主体功能区规划相衔接",
    "环境保护规划的内容应当与城乡规划等相衔接",
    2,
]
str_test[110] = [
    "下面描述不正确的是",
    "无国家环境质量标准的地方政府可以制定地方环境质量标准",
    "省、自治区、直辖市人民政府可以制定严于国家环境质量标准地方标准",
    "省、自治区、直辖市人民政府可以制定低于国家环境质量标准地方标准",
    "地方环境质量标准应当报国务院环境保护主管部门备案",
    3,
]
str_test[111] = [
    "下面那一条不是跨行政区域的重点区域、流域环境污染和生态破坏联合防治协调机制",
    "统一规划",
    "统一标准",
    "统一监测",
    "统一设备",
    4,
]
str_test[112] = [
    "企业事业单位和其他生产经营者违反法律法规规定排放污染物，造成严重污染的，县级以上人民政府环境保护主管部门可以进行的事项描述中，哪项是正确的？",
    "可以查封、扣押造成污染物排放的设施、设备，但必须在当地法院人员陪同下进行",
    "可以查封、扣押造成污染物排放的设施、设备，但必须在当地公安人员陪同下进行",
    "无权查封、扣押造成污染物排放的设施、设备",
    "可以查封、扣押造成污染物排放的设施、设备",
    4,
]
str_test[113] = [
    "建设项目中防治污染的设施，应当与（  ）同时设计、同时施工、同时投产使用",
    "关键工程",
    "附属工程",
    "主体工程",
    "重要工程",
    3,
]
str_test[114] = [
    "下面关于排污费描述错误的是哪一条",
    "排污单位应当按照国家有关规定缴纳排污费",
    "排污费应当全部专项用于环境污染防治",
    "排污单位已依照法律规定征收环境保护税的，不再征收排污费",
    "排污单位所缴纳排污费可以按一定的比例返纳给排污单位用于污染治理",
    4,
]
str_test[115] = ["重点污染物排放总量控制指标由（      ）下达。", "省人民政府", "直辖市人民政府", "国务院", "自治区人民政府", 3]
str_test[116] = [
    "下面关于排污许可证描述错误的是哪一条？",
    "国家依照法律规定实行排污许可管理制度",
    "已取得排污许可证的，只要排放污染物总量不超标，允许排放许可证许可范围外的其它污染物",
    "实行排污许可管理的单位应当按照排污许可证的要求排放污染物",
    "未取得排污许可证的，不得排放污染物",
    2,
]
str_test[117] = ["农村生活废弃物的处置工作由（       ）人民政府负责组织", "地区级", "县级", "乡级", "省级", 2]
str_test[118] = ["提起环境损害赔偿诉讼的时效期间为（   ）。", "三年", "一年", "二年", "五年", 1]
str_test[119] = [
    "建设项目未依法进行环境影响评价，被责令停止建设，拒不执行的，对其直接负责的主管人员，情节较轻的，处（     ）。",
    "十日以上十五日以下拘留",
    "七日以上十五日以下拘留",
    "五日以上十五日以下拘留",
    "五日以上十日以下拘留",
    4,
]
##答案
for i in range(20):
    answer[i + 100] = str_test[i + 100][5]

global n, num, step, test_num
n = 0
num = 20
step = 1
# li = list(np.arange(0, 100))
# 从列表 items 中随机取出100 个元素，但不改变原列表。

add_selectbox = st.sidebar.radio(
    "选择做题内容", ("隐患排查与治理", "法律法规", "各类标准", "信访回复", "检测与争议", "综合")
)
if add_selectbox == "隐患排查与治理":
    name_test = "隐患排查与治理"
    sel_no = 1
    test_num = 18
    # st.subheader("本次答题内容为隐患排查与治理")
elif add_selectbox == "各类标准":
    name_test = "各类标准"
    sel_no = 2
    test_num = 18
elif add_selectbox == "法律法规":
    name_test = "法律法规"
    sel_no = 2
    test_num = 18


elif add_selectbox == "信访回复":
    name_test = "信访回复"
    sel_no = 2
    test_num = 18
elif add_selectbox == "检测与争议":
    name_test = "检测与争议"
    sel_no = 2
    test_num = 18
elif add_selectbox == "综合":
    name_test = "综合"
    sel_no = 2
    test_num = 18


# step=1#调试用
st.header("基层生态环境工作人员培训知识考试")
str_testname = "本次考试内容为" + add_selectbox
st.subheader(str_testname)
st.subheader("点击左上角的→可选择考试内容")

st.text("本软件代码由方利国开发,发现错误之处请联系lgfang@scut.edu.cn,不胜感谢。")
st.text("点击左上方的>可以选择考试内容")
name = st.text_input("请输入您的姓名", "张三")
dt = datetime.datetime.now() + datetime.timedelta(hours=8, minutes=0, seconds=-22)
st.subheader("当前时间" + str(dt))

if "time1" not in st.session_state:
    st.session_state.time1 = None
if "time2" not in st.session_state:
    st.session_state.time2 = None

# 按钮
if st.button("请在开始答题时点击我，做完题目再点击一次，马上点击提交"):
    # 如果time1是空的，记录第一次点击的时间
    if st.session_state.time1 is None:
        st.session_state.time1 = time.time()
        # datetime.now()
        # st.write("记录第一次点击的时间: ", st.session_state.time1)
    # 否则记录第二次点击的时间，并计算时间间隔
    elif st.session_state.time2 is None:
        st.session_state.time2 = time.time()
        # datetime.now()
        interval = st.session_state.time2 - st.session_state.time1
        # st.write("记录第二次点击的时间: ", st.session_state.time2)
        h = interval // 3600  ##计算小时
        h_s = interval % 3600
        m = h_s // 60  ##计算分钟
        s = h_s % 60  ##计算秒
        # str_time = "考试用时" + str(time_use) + "秒"
        # st.subheader(str_time)
        st.write("本次答题时间为: ", h, "小时", m, "分钟", s, "秒")
        st.subheader("本次答题时间为:" + str(interval) + "秒,请截屏保存，并马上点击后面的提交按钮")

        # 重置时间记录，准备下一次计时
        st.session_state.time1 = None
        st.session_state.time2 = None


with st.form("my_form"):
    for i in range(test_num):
        str_k = "第" + str(i + 1) + "题"
        st.subheader(str_k)
        # k=test_num[i]
        k = i * step + (sel_no - 1) * 100
        k = int(k)
        select = st.radio(
            str_test[k][0],
            (str_test[k][1], str_test[k][2], str_test[k][3], str_test[k][4]),
            horizontal=True,
        )  # 前面题目，后面4个选项
        if select == str_test[k][str_test[k][5]]:
            # [answer[k]]:  # 这里填正确答案,目前题目从0-1199
            n = n + 1
        # print(str_test[k][5])
    if sel_no == 1:
        str_k = "第" + str(19) + "题"
        st.subheader(str_k)
        options = st.multiselect(
            "环境安全隐患排查中常说的“三口一池”是指",
            ["初期雨水池", "环境事故应急池", "围堰等设施场所的排水管道口", "企业污水总排口", "企业雨水总排口", "企业设备冷凝水总排口"],
        )
        if options == ["环境事故应急池", "围堰等设施场所的排水管道口", "企业污水总排口", "企业雨水总排口"]:
            n = n + 1
        str_k = "第" + str(20) + "题"
        st.subheader(str_k)
        options = st.multiselect(
            "企业环境安全隐患治理中的四自是指",
            ["自查", "自建", "自报", "自写 ", "自改", "自验"],
        )
        if options == ["自查", "自报", "自改", "自验"]:
            n = n + 1

    if sel_no == 2:
        str_k = "第" + str(19) + "题"
        st.subheader(str_k)
        options = st.multiselect(
            "县级以上人民政府环境保护主管部门和其他负有环境保护监督管理职责的部门，应当依法公开的信息有",
            ["环境质量", "环境监测", "环境行政许可及行政处罚", "企业技术水平", "企业经济状况"],
        )
        if options == ["环境质量", "环境监测", "环境行政许可及行政处罚"]:
            n = n + 1
        str_k = "第" + str(20) + "题"
        st.subheader(str_k)
        options = st.multiselect(
            "重点排污单位应当如实向社会公开其",
            [
                "主要污染物的名称",
                "主要生产工艺",
                "关键生产设备",
                "污染物排放方式 ",
                "污染物排放浓度和总量",
                "防治污染设施的建设和运行情况",
            ],
        )
        if options == ["主要污染物的名称", "污染物排放方式 ", "污染物排放浓度和总量", "防治污染设施的建设和运行情况"]:
            n = n + 1

    submitted = st.form_submit_button("点击提交")
    if submitted:

        # end_time = time.time()
        # end_time = time.process_time()
        # time_use = end_time - start_time
        # con_num=1
        str_finsh = "欢迎您" + name + ",已完成考试,试卷内容为" + name_test
        st.subheader(str_finsh)
        # str_time = "考试用时" + str(time_use) + "秒"
        # st.subheader(str_time)
        # for i in range(num):
        # k=test_num[i]
        # if select ==str_test[k][answer[k-100]] :  #这里填正确答案,目前题目从100 199
        # n=n+1
        # st.write("本次答题时间为: ", h, "小时", m, "分钟", s, "秒")
        # st.subheader("本次答题时间为:" + str(interval) + "秒")
        if n / num > 0.9:
            str_n = str(n)
            sstr = (
                "恭喜您答对"
                + str_n
                + "题,答对率为"
                + str(int(100 * 100 * n / num + 0.5) / 100)
                + "%，是个生态环境工作大行家"
            )
            st.subheader(sstr)
            # st.experimental_rerun()
        elif n / num > 0.6:
            str_n = str(n)
            sstr = (
                "恭喜您答对"
                + str_n
                + "题,答对率为"
                + str(int(100 * 100 * n / num + 0.5) / 100)
                + "%，本次成绩不错，还有提升空间"
            )
            st.subheader(sstr)
            # st.experimental_rerun()
        elif n / num <= 0.6:
            str_n = str(n)
            sstr = (
                "本次只答对"
                + str_n
                + "题,答对率为"
                + str(int(100 * 100 * n / num + 0.5) / 100)
                + "%，成绩不理想，请多多学习"
            )
            st.subheader(sstr)
        fig = plt.figure(num="Correct Answer Chart", figsize=(8, 8))
        labels = ["Correct", "Mistake"]
        C_M_data = [n / num, 1 - n / num]  # 正确与错误数据
        colors = ["lightblue", "red"]  # 颜色
        explode = (0.1, 0.1)  # 间隔距离，半径的比例
        plt.pie(
            C_M_data,
            explode=explode,
            labels=labels,
            startangle=45,
            shadow=True,
            colors=colors,
            autopct="%3.1f%%",
        )
        # st.subheader("*******答题对错率图******")
        plt.title("Question Answering Correct and Mistake Rate Chart")

        st.pyplot(fig)
        dt = datetime.datetime.now() + datetime.timedelta(
            hours=8, minutes=4, seconds=-22
        )
        st.subheader("当前时间" + str(dt))
        str_finsh1 = str_finsh + "请截屏成绩发给指定人员或地址"
        sstr = (
            "本次只答对"
            + str(n)
            + "题,答对率为"
            + str(int(100 * 100 * n / num + 0.5) / 100)
            + "%"
        )
        sstr = sstr + str_finsh1
        add_selectbox = st.sidebar.subheader(sstr)
        add_selectbox = st.sidebar.subheader("##若要继续考试可重新选择左边的答题内容##")
