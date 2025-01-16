# def show1(x, y):
#     print(x, y)
# show1(100,200)

# def show2(x, y):
#     print(x, y)
# show2(y =100,x =200)

# def show(x, y=300):
#     print(x, y)
# show(100)

# def show(*args):
#     print(args[1],args[0])
# show(100,200)

# def show(*args):
#     print(args)
#     for i in args:
#         print(i)
# show(100,200)

# def show(**args):
#     for i in args:
#         print(i)
# show(y=100, x=200)

# def show(**args):
#     print(args["a"], args["b"])
# show(b=100, a=200)

# ======================= global==================
# x = 100
# def show():
#     global y
#     y = 20
#     print(y)
# show()

# print("y is used form locally with use of global keyword: ",y)

# =======================globals===================
x = 100
def show():
    y = 20
    x = 150 # agar ye 150 vala x niche likh diya tho x ka latest value jo hoga vahi lenhge 
    x = globals()["x"]
    print("global x ka value locally use:",x)
    print("ye local y hi hai:",y)
    
show()