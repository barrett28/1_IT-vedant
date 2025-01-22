def empty_or_not():
    n = int(input("enter length: "))
    n_list=[]
    
    if n==0:
        print("empty")
        return
        
    
    for i in range(n):
        ele = input(f"enter something to be inserted in list {i+1}/{n}: ")
        n_list.append(ele)
        
        if len(n_list)>0:
            print("NOT EMPTY")
            
empty_or_not()