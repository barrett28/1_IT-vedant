# s = "bharat"
# rev = ""
# for i in s:
#     rev = i +rev
# print(rev) 

# s = "ye ek string hai"
# s1 = s.split()
# for i in s1:
#     print(s1.index(i))
#     if s1.index(i)%2==0:
#         print(s1)


# s = "ye meri string hai"
# s1 = s.split()
# print(s1)
# for i in range(len(s1)):
#     # print(i)
#     if  i%2==0:
#         print(s1[i])
#         s1[i]=""
# print(s1)
# ==========================================
# s = "itvedantpyhtonbatch"
# s = input("enter string:")
# for i in range(len(s)):
#     if len(s)<6:
#         print("empty string")
#     else:
#         s1 = s[0:3]
#         s2 = s[-3:]
#         s3 = s1+s2
#     print(s3)
#     break
# ===========================================
s = input("Enter a string: ")

if len(s) < 6:
    print("Empty string")
else:
    s1 = s[:3]  # First 3 characters
    s2 = s[-3:] # Last 3 characters
    s3 = s1 + s2
    print(s3)



