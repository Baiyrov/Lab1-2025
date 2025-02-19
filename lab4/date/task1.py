from datetime import datetime, timedelta

x=datetime.now()
new=x-timedelta(days=5)


print(x.strftime("%Y-%m-%d"))
print(new.strftime("%Y-%m-%d"))