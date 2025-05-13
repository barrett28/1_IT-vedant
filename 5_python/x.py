# l = [1,2,3,4]
# l1 = l[0]
# l2 = l[1]
# for i in l:
#     for j in l:
#         if i>j:
#             l2 = j
#             l1 = i

# j = max(l)
# print(j)


"""
5****
*4***
**3**
***2*
****1
"""

# x = 5

# for i in range(1, x+1):
#     star = i-1
#     space = '5'
#     ts = x-i
#     print('*'*star + space + "*"*ts)



# a,b,c,d = 5,4,8,16


# if b>a and b>c and b>d:
#     max = b
# elif c>b and c>a and c>d:
#     max = c
# elif d>c and d>b and d>a:
#     max = d
# else:
#     max = a
# print(max)

# w = "level civic palindrome"
# list = []
# w1 = w.split()

# for i in w1:
#     i1 = i[::-1]
#     list.append(i1)

# for j in w1:
#     for k in list:
#         if j == k:
#             print(j)

# l = [10,20,30,40,20,20,50]

# l2 = []

# for i in l:
#     if i not in l2:
#         l2.append(i)
        
# print("new list ",l2)
# print("prior list",l)


# l = [4,9,56,16,19,34]

# a = float('-inf')
# b = float('-inf')

# for i in l:
#     if i > a:
#         b = a
#         a = i
#     elif i > b and i < a:
#         b = i
        
# l = [4,9,56,16,19,34]
# for i in range(0, len(l)):
#     for j in range(i+1, len(l)):
#         if l[i] > l[j]:
#             l[i], l[j] = l[j], l[i]
# print(l, "->",l[-2])

# l = [10, 30, 45, 20, 5, 45]

# a = float("-inf")
# b = float("-inf")

# for n in l:
#     if n>a:
#         a = n
# print("a", a)

# for n in l:
#     if n>b and n<a:
#         b = n
# print("b", b)
        
# print("second highest ",b)
# print(l)



x = 20

for i in range(1,x+1):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)