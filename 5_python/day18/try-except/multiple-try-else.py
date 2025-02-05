x = 100
y = 20

try:
    z = x/y
    print(z)
except ZeroDivisionError as z:
    print("error",z)
else:
    print("try chal gaya")
finally:
    print("me tho run hoke hi rahunga")
    
    