# a = int(input("enter 1st number:"))
# b = int(input("enter 2nd number:"))
# c = int(input("enter 3rd number:"))
# d = int(input("enter 4th number:"))

# if a > b and a > c and a > d:
#     print(a, "is greatest")
# elif b > a and b > c and b > d:
#     print(b, "is greatest")
# elif c > a and c > b and c > d:
#     print(c, "is greatest")
# elif d > a and d > b and d > c:
#     print(d, "is greatest")
# else:
#     print("tie")


# a = int(input("enter 1st number:"))
# b = int(input("enter 2nd number:"))
# c = int(input("enter 3rd number:"))
# d = int(input("enter 4th number:"))

# if a > b and a > c and a > d:
#     print(a, "is greatest")
# elif b > c and b > d:
#     print(b, "is greatest")
# elif c > d:
#     print(c, "is greatest")
# else:
#     print(d, " d is greater")
    


# a = int(input("enter 1st number:"))
# b = int(input("enter 2nd number:"))
# c = int(input("enter 3rd number:"))

# if a==b==c:
#     print("equal")
# else:
#     print("not equal")
    
    
# ============== month se date ana chahiye 
# ============== 5 6 7 increasing order , 9 8 7 decreasing order


# a = int(input("enter number of your month: "))

# if a>12 or a<=0:
#     print("invalid month")
# elif a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12:
#     print("31")
# elif a==2:
#     print("28")
# else:
#     print("30")

# ==============================


# n1 = int(input("enter number:")) #5 7
# n2 = int(input("enter number:")) #6 6
# n3 = int(input("enter number:")) #7 5

# if (n2-n1==1 and n3-n2==1) and  n1>n2>n3:
#     print("decreasing order")
# elif (n1-n2==1 and n2-n3==1) and n3>n2>n1:
#     print("increasing order")
# else:
#     print("not on any order")



n1 = int(input("enter number:")) #5 7
n2 = int(input("enter number:")) #6 6
n3 = int(input("enter number:")) #7 5

if (n2 - n1 == 1 and n3 - n2 == 1):
    print("increasing order")
elif (n1 - n2 == 1 and n2 - n3 == 1):
    print("decreasing order")
else:
    print("not on any order")