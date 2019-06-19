year = int(input("请输入年份:\n"))
month = int(input("请输入月份:\n"))
day = int(input("请输入日期:\n"))
days = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
current_day = 0
if 0 < month <= 12:
    current_day += days[int(month-1)]
    current_day += day
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    if month > 2:
        current_day += 1
print(current_day)
