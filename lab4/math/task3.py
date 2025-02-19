import math

a=int(input())
b=int(input())  

area=(a*b**2)/(4*math.tan(math.pi/a))

print(format(area, ".2f"))