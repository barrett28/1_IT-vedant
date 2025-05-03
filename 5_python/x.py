l = [1,2,3,4]
# l1 = l[0]
# l2 = l[1]
# for i in l:
#     for j in l:
#         if i>j:
#             l2 = j
#             l1 = i

j = max(l)
print(j)


"""
5****
*4***
**3**
***2*
****1
"""

x = 5

for i in range(1, x+1):
    star = i-1
    space = '5'
    ts = x-i
    print('*'*star + space + "*"*ts)
        