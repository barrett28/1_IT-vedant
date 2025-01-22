def greater_than3():
    n = int(input("enter the length of loop: "))
    n_list=[]
    
    for i in range(n):
        ele = input(f"enter here {i+1}/{n}: ")
        if ele.isdigit():
            ele=int(ele)
            n_list.append(ele)
        
        # for j in range(len(n_list)):
        #     if n_list[j]>3:
        #         print(n_list)
        
    # for j in n_list:
    #     if j>3:
    #         print(j)
    
    greater_than_three = [j for j in n_list if j>3]
    print("the values which are greater than 3: ", greater_than_three)
    print("count of the values: ", len(greater_than_three))
    

greater_than3()