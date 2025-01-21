def not_in_b():
    n1 = int(input("enter length of l1: "))
    n2 = int(input("enter length of l2: "))
    n1_list=[]
    n2_list=[]
    
    for i in range(n1):
        ele = input(f"enter element in list1 {i+1}: ")
        n1_list.append(ele)
        
    for j in range(n2):
        ele1 = input(f"enter element in list2 {j+1}: ")
        n2_list.append(ele1)
        
    not_common=[]
    for k in n1_list:
        if k not in n2_list:
            not_common.append(k)
            print("element not present in 2nd list are :", not_common)
        else:
            print("empty", not_common)

not_in_b()