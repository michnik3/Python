from pkg.examples import my_tuple
l1 = []
for i in range(10):
    user_input = int(input("Dwse akeraio aithmo: "))
    while user_input < 10 or user_input > 20:
        user_input = int(input("Dwse akeraio aithmo: "))
    
    l1.append(user_input)

print(l1)


my_tuple = tuple(l1)
print(my_tuple)

list_squares = []
for i in range(10):
    list_squares.append(l1[i] ** 2)

list_squares.sort()
tuple_squares = tuple(l1_squares)
print(tuple_squares)

'''
Created on Dec 7, 2020

@author: Michel
'''
