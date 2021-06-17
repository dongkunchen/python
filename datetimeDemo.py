'''
datetime比time高級了不少,可以理解為datetime基於time進行了封裝
提供了各未使用的函數 datetime模塊的接口更直觀,更容易調用
模塊中的類:
datetime 同時有時間和日期
timedelta 主要用於計算時間的跨度
tzinfo 時區相關
time 只關注時間
date 只關注日期
'''
import datetime

#獲取當前時間
d1 = datetime.datetime.now()
print(d1)
print(type(d1))

#獲取指定時間
d2 = datetime.datetime(1999,10,1,10,28,25,123456)
print(d2)

#將時間轉為字符串
d3 = d1.strftime("%Y-%m-%d %X")
print(d3)
print(type(d3))

#將各式化字符串轉為datetime對象
#注意:轉換的格式要與字符串一致
d4 = datetime.datetime.strptime(d3,"%Y-%m-%d %X")
print(d4)

d5 = datetime.datetime(1999,10,1,10,28,25,123456)
d6 = datetime.datetime.now()
d7 = d6 - d5
print(d7)
print(type(d7))
#間隔的天數
print(d7.days)
#間隔天數除外的秒數
print(d7.seconds)
