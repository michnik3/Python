list_int = [8,6,4]

if list_int[0] > list_int[1] and list_int[0] > list_int[2]:
    print(list_int[0])
elif list_int[1] > list_int[0] and list_int[1] > list_int[2]:
    print(list_int[1])
else:
    print(list_int[2])

print(list_int)

#deyteros tropos pio swstos

numbers = [2, 1, 0]

maximum = numbers[0]

if numbers[1] > maximum:
    maximum = numbers[1]

if numbers[2] >maximum:
    maximum = numbers[2]

print(maximum)