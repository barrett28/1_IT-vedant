def as_it_is():
    n = int(input("enter length of list: "))
    n_list=[]
    
    for i in range(n):
        ele = input(f"enter something to add in list {i+1}/{n}: ")
        
        if ele.isdigit():
            ele = int(ele)
        elif ele.replace(".","").isdigit() and ele.count(".")==1:
            ele = float(ele)
        else:
            ele = str(ele)
            
        n_list.append(ele)
        print("entered element is ", ele, "and its type is ", type(ele))
    return n_list 
    
print(as_it_is())