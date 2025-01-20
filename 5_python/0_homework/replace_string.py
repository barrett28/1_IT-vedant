# print("replaced string question")



# s = input("enter string:")

# old=input("enter the old character: ")
# new=input("enter the new character: ")
# if old not in s:
#     print("string does not contain that character")
# else:
#     s1 = s.replace(old, new)
#     print(s1)
    
def replace_char(s, old_char, new_char):
    s1 = s.replace(old_char, new_char)
    return s1
    
s = input("enter a string:")
old_char=input("enter the old character which you want to change:")
new_char=input("enter the new character:")

print(replace_char(s, old_char, new_char))