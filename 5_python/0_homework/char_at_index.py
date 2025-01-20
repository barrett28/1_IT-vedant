def char_at_index(s, index):
    if s not in s:
        print("out of range")
    else:
        print(s[index])
            

s = str(input("enter a string: "))
index = int(input("enter index number: "))
char_at_index(s, index)