def largest_num():
    n = int(input("enter the length of loop: "))
    n_list=[]
    
    for i in range(n):
        ele = input(f"enter here {i+1}/{n}: ")
        n_list.append(ele)
        n_list.sort()
    print("this is your list: ",n_list)
    if len(n_list)>1:
        print("2nd highest number is: ",n_list[-2])
    else:
        print("None")

largest_num()