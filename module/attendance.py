#2018/05/05

from datetime import datetime
import os


print("★" + str(os.getcwd()))

now = datetime.now()
str_now = now.strftime('%Y/%m/%d %H:%M')


with open("./module/output/attendance.log", "a", encoding="utf-8") as f:
    if 6 <= now.hour < 14:
        f.write(str_now + " - 出勤\n")
    else:
        f.write(str_now + " - 退勤\n")
print('書き込み完了')