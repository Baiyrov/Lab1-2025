from datetime import datetime

x=datetime.now()
a=x.replace(microsecond=0)

print(x)
print(a)