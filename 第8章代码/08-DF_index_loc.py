# DataFrame 索引和排序
import numpy as np
import pandas as pd

dict = {
    "city": ["A城", "B城", "C城", "D城", "E城", "F城"],
    "GDP": [12390, 10890, 1900, 8901, 7821, 6532],
    "Population": [103, 98, 160, 102, 98, 89],
    "Incre_rate": [1.4, 2.1, -1.5, 3.2, 3.1, 0.8],
}
DF = pd.DataFrame(dict)  # 字典数据创建DF
print(DF)
DF = DF.set_index(["city"])  # 设置city为索引
print(DF)
# print(DF.info())
print("DF.loc['A城']:\n", DF.loc["A城"])  # lo函数c横向索引A城数据
print("DF.GDP\n", DF.GDP)  # 纵向索引GDP的数据
print("DF.GDP.C城:\n", DF.GDP.C城)  # 精确定位索引C城的GDP数据
print("DF.['GDP']\n", DF["GDP"])  # 纵向索引GDP的数据
print("DF.values[(0,2)]=", DF.values[(0, 2)])  # 利用values的行、列序号索引任意数据
print("DF. Population.B=", DF.Population.B城)


# 下面通过文件读入2020年GDP前50城市数据进行分组、排序

filename = "g:\city_gdp.xls"
DF3 = pd.read_excel(filename, "Sheet1", na_filter=False, index_col=0)
print(DF3)
print(DF3.province.value_counts())  # 统计省份数据
DF_province_top6 = DF3.province.value_counts().head(6)
print("DF_province_top6:\n", DF_province_top6)  # 打印进入前50城市数目前6的省份数据

print("DF3.head(6)前6行数据:\n", DF3.head(6))  # 打印前6行数据
print("DF3.tail(6)最后6行数据:\n", DF3.tail(6))  # 打印最后6行数据

print(
    "DF3.set_index('province').sort_values('GDP'):\n",
    DF3.set_index("province").sort_values("GDP"),
)

DF4 = DF3.set_index(["province", "city"])

print("DF4.loc['浙江']:\n", DF4.loc["浙江"])
print("DF4.loc[('浙江','宁波')]:\n", DF4.loc[("浙江", "宁波")])

print(
    "GDP省总和排序:\n",
    DF4.drop("number", axis=1)
    .sum(level="province")
    .sort_values("GDP", ascending=False),
)

print(
    "GDP省上榜城市平均值排序:\n",
    DF4.drop("number", axis=1)
    .mean(level="province")
    .sort_values("GDP", ascending=False),
)

print(
    DF4.drop("number", axis=1)
    .groupby("province")
    .sum()
    .sort_values("GDP", ascending=False)
)
