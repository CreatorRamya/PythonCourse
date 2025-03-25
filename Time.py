from datetime import date, time, datetime

today = date.today()
now = datetime.now()

print("Today's date is", today)
print("\n Current date and time is", now)

print("\nDate components", today.day, today.month, today.year)

import calendar

yy = 2011
mm = 6
dd = 11

print(calendar.month(yy,mm,dd))




import datetime

x = datetime.datetime.now()
print(x)