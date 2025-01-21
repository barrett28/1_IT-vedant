# ele = [1,2,3,4,5]

# el1 = set(*[ele])
# # print(el1)


set1 = {1,2,3,4}
set2 = {4,5,6,7}

s = set1.union(set2)
# print("union: ",s)

s1 = set1.intersection(set2)
# print("intersection",s1)

s2 = set1.intersection_update(set2)
# print(s2)
# print(set1)

s3 = set2.add("hello")
# print(set2)

s4 = set2.remove(4)
# print(set2)

