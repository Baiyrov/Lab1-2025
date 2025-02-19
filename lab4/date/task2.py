from datetime import datetime, timedelta

x=datetime.now()
a=x-timedelta(days=1)
b=x+timedelta(days=1)

print(x.strftime("%Y-%m-%d"))
print(a.strftime("%Y-%m-%d"))
print(b.strftime("%Y-%m-%d"))