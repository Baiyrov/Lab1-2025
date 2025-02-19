def num(x):
    for num in range (0,x+1):
        if num%3==0:
            if num%4==0:
                yield str(num)

x= int(input())

print(",".join(num(x)))