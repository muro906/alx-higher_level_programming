l1 = [1,2,3]
l2 = [4,5,6]
print(id(l2))
print(id(l1))
l1 = l2
print(l1 is l2)
print(l1)