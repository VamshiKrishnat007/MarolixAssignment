
# print the time left the next new year
from datetime import datetime, timedelta

input1=input()
datetime_ob=datetime.strptime(input1,"%b %d %Y %I:%M %p")
date_2=datetime(datetime_ob.year,month=12,day=31,hour=12)

dur=(date_2-datetime_ob).days
print("{} Hours {} Minutes".format(dur*24,""))



#Jan 31 2020 04:43 AM
# 33 hours 17 minutes