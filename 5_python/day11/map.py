l = [1,2,3,4]

def square(x):
    return x**2

x = map(square, l)
y = list(x)
print(y)