
# print the time left the next new year
from datetime import datetime, timedelta

from datetime import datetime, timedelta,time
input1=input()
date_obj=datetime.strptime(input1,"%b %d %Y %I:%M %p")
date_obj2=datetime(date_obj.year+1,month=1, day=1)

days=(date_obj2-date_obj)
hours=days.days*24+days.seconds//3600
minutes=(days.seconds//60)%60
print("{} hours {} minutes".format(hours,minutes))



#Jan 31 2020 04:43 AM
# 33 hours 17 minutes