def num(x):
    for num in range (x+1,0, -1):
        yield str(num)

x= int(input())

print(",".join(num(x)))