def square (x):
    for num in range (1, x+1):
        yield num**2

x= int(input()) 
for square in square(x):
    print(square)