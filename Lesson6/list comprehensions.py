my_list = []
for number in range(10):
    if number % 2 ==0:
        my_list.append(number)
print(my_list)

my_list = [number for number in range(10) if number % 2 == 0]
print(my_list)

print("=====================")

my_list = [number if number % 3 == 0 else number/2 for number in range(10)]
print(my_list)
