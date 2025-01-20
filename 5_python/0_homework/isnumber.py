def is_num(s):
    for i in s:
        if i.isdigit():
            return True
    return False

s = str(input("enter to check if numbers are present or not:"))
print(is_num(s))