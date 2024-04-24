from datetime import datetime
import time

dt1 = datetime(2022, 1, 1)
print(dt1)

dt2 = datetime.now()
print(dt2)

print(dt2 > dt1)

dt = datetime.strptime("2018/01/02", "%Y/%m/%d")
print(dt)

dt = datetime.fromtimestamp(time.time())
print(dt)

print(f"{dt.year}/{dt.month}/{dt.day}")

print(dt.strftime("%Y/%m"))
