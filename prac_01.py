import datetime

today= datetime.date.today()
month = int(input("which month do you born? "))
day = int(input("which day do you born? "))
birthday = datetime.date(today.year, month, day)

if birthday < today:
    birthday = datetime.date(today.year + 1, month, day)

diff = birthday - today
if diff.days == 0:
    print("Happy birthday!!!")
else:
    print("挖! 再過" + str(diff.days) + "天就是你的生日啦!")
