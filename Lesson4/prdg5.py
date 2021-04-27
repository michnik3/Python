l1 = [1, 2, 3]
l1.append(4)
print(l1)

print("------------------")

l2 = [1, 2, 3]
l2.insert(1,4)
print(l2)

print("------------------")

l3 = [1, 2, 3]
l3.extend([5,8])
print(l3)

print("------------------")

l4 = [1, 2, 3]
last = l4.pop()
print(last)
print(l4)
l4.pop(0)
print(l4)

print("------------------")

l5 = [1, 2, 3, 2, 4]
print(l5)
l5.remove(2)
print(l5)

print("------------------")

l6 = [1, 2, 3]
print(l6)
l6.clear()
print(l6)
