def even(x):
    for num in range (0,x+1, 2):
        if num%2==0:
            yield str(num)

x= int(input())

print(",".join(even(x)))