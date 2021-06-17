import calendar
'''
日曆模塊

'''
#使用
#返回指定某年某月的日曆
print(calendar.month(2021,4))
# 返回指定年的日曆
# print(calendar.calendar(2017))
# 閏年返回True,否則返回False
# print(calendar.isleap(2000))

#返回某個月的weekday的第一天和這個月的天數
print(calendar.monthrange(2021,4))

print(calendar.monthcalendar(2021,4))
