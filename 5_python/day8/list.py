# f = [1,2,3]
# t = [4,5,6]

# f.extend(t)
# print(f)

# def input_user(s, s_list):
#     s_list.append(s)
#     return s_list

# s = input("add in list: ")
# s_list=[]
# print(input_user(s, s_list))


def insert_times():
    n = int(input("length of list: "))
    s = []
    for i in range(n):
        ele = input(f"enter you want to enter into the list:{i+1} ")
        s.append(ele)
    return s


t = insert_times()
print(t)