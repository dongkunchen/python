#list-->set
l1 = [1,2,3,4,5,3,4,5]
s1 = set(l1)

#tuple-->set
t2 = (1,2,3,4,3,2)
s2 = set(t2)

#set-->list
s3 = {1,2,3,4}
l3 = list(s3)
print(l3)

#set-->tuple
s4 = {2,3,4,5}
t4 = tuple(s4)
print(t4)

#list去重
l = [1,2,3,4,3,4,5,6]
# s = set(l)
# l = list(s)
# print(l)
l = list(set(l))
print(l)