from datetime import datetime

x=datetime(2025,2,15,12,0,0)
a=datetime(2025,2,10,8,30,0)

difference=(x-a).total_seconds()

print(difference)