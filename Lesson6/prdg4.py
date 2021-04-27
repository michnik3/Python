'''
Created on Dec 7, 2020

@author: Michel
'''
#list.copy.problem
l1 = [1, 2, 3]
l2 = l1
l2[0] = 4
print(l1)
print(l2)

print("============")

l1 = [1, 2, 3]
l2 = l1[:]
l2[0] = 4
print(l1)
print(l2)