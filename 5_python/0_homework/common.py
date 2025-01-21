def common():
    n1 = int(input("length of list1: "))
    n2 = int(input("length of list2: "))
    n1_list = []
    n2_list = []
    
    for i in range(n1):
        ele = input(f"enter for list1:{i+1} ")
        n1_list.append(ele)
    for i2 in range(n2):
        ele1 = input(f"enter for list2:{i2+1} ")
        n2_list.append(ele1)  
        
    common_ele = [] 
    if i in range(n1):
        for j in range(n2):
            if n1_list[i]==n2_list[j]:
                # print("")
                common_ele.append(n1_list[i])
                print(common_ele)
                 
    return n1_list, n2_list,common_ele
            
t = common()
print(t)


