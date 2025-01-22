def sec_small_num():
    n = int(input("enter the length of loop: "))
    n_list=[]
    
    for i in range(n):
        ele = input(f"enter here {i+1}/{n}: ")
        n_list.append(ele)
        n_list.sort()
    print("this is your list: ",n_list)
    if len(n_list)>1:
        print("2nd smallest number is: ",n_list[1])
    else:
        print("None")

sec_small_num()