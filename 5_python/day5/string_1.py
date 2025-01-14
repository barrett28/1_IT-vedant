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


s = "ye meri string hai"
s1 = s.split()
print(s1)
for i in range(len(s1)):
    # print(i)
    if  i%2==0:
        print(s1[i])
        s1[i]=""
print(s1)


