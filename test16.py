import datetime
import time
if __name__ == '__main__':
    # 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
    print(time.strftime('%Y-%m-%d %H:%M:%S'))

    # 创建日期对象
    miyazakiBirthDate = datetime.date(2009, 6, 20)

    print(miyazakiBirthDate.strftime('%Y-%m-%d'))
    print(datetime.date(2009,1,2))
    # 日期算术运算
    miyazakiBirthNextDay = miyazakiBirthDate + datetime.timedelta(days=1)

    print(miyazakiBirthNextDay.strftime('%Y-%m-%d'))

    # 日期替换
    miyazakiFirstBirthday = miyazakiBirthDate.replace(year=miyazakiBirthDate.year + 1)

    print(miyazakiFirstBirthday.strftime('%Y-%m-%d'))