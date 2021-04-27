while True:
    string = input("Give name: ")
    string = string.strip()



    if string.isalpha():
        name = string.capitalize()

        print(f"Name entered: {name}")
        break
    else:
        print("only characters please! ")

while True:
    string = input("Give last name: ")
    string = string.strip()



    if string.isalpha():
        last_name = string.capitalize()

        print(f"last name entered: {last_name}")
        break
    else:
        print("only characters please! ")

print(f"+{28 * '-'}+")
print(f"|{(name +' '+ last_name).center(28)}|")
print(f"+{28 * '-'}+")