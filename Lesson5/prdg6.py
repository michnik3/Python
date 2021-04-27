number = int(input("Enter a number(0-9): "))

while number < 0 or number > 9:
    number = int(input("Enter a number(0-9) again: "))

print("You entered a right value.")