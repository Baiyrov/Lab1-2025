def squares(x,y):
    for num in range (x,y+1):
        yield num**2

x= int(input())
y= int(input())

for square in squares(x,y):
    print(square)