# 制作中文日历35-makecalendar.py
import calendar
print(calendar.month(2021, 3))
print(calendar. calendar(2021))
calendar.isleap(2021)
calendar.monthcalendar(2021, 3)
calendar.prcal(2020, w=0, l=0, c=6, m=3)


def pri_calen(k, ws, day):
    if day > 10:
        print(f"{int(3+k*7)*ws}{day}", end="")
    else:
        if day == 10:
            print(f"{int(4+k*7)*ws}{day}", end="")
        else:
            print(f"{int(3+k*8)*ws}{day}", end="")


year = eval(input("请输入需要制作日历的年份，输入后请回车year="))
print("{:>29}".format("2021年日历"))
for i in range(1, 13):
    mlist = calendar.monthcalendar(year, i)
    print("")
    print("{:>27d}".format(i), "月")
    print("")
    print("星期日  星期一  星期二  星期三  星期四  星期五  星期六 ")
    ww = len(mlist)
    for w in range(ww):
        k = 0
        for d in range(7):
            day = mlist[w][d]
            if day == 0:
                k = k + 1
                continue
            ws = " "
            if d == 0:
                print(f"{3*ws}{day}", end="")
                k = 0.51  # 预防精度问题影响取整函数
            else:
                pri_calen(k, ws, day)
                k = 0.51
        print("")
