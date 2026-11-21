# 假设一个任务的创建时间是 "2026-11-18 10:00:00"。
#
# 获取当前时间，计算这个任务已经创建了多少个小时了。
#
# 如果超过了 48 小时，打印 "任务已超时"，否则打印
from datetime import datetime, timedelta


date_str = "2026-11-18 10:00:00"
format_date = "%Y-%m-%d %H:%M:%S"
create_time = datetime.strptime(date_str, format_date)
current_time = datetime.now()
time_difference = current_time - create_time
if time_difference > timedelta(hours=48):
    print("任务已超时")
else:
    print("任务未超时")


