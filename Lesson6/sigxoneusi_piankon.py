marinalist = []

while True:

    a = input("ship name")
    b = input("owner name")
    while True:
        type_boat = input("Give type of boat :")
        if type_boat == "narrow":
            print("Correct Type, your type is narrow")
            break
        elif type_boat == "sailing":
            print("Correct Type, your type is sailing")
            break
        elif type_boat == "motor":
            print("Correct Type, your type is motor")
            break
    d = input("boat length")
    if "esc" in (a,b,type_boat,d):
        print("exiting in program")
        break

    templ = [a,b,type_boat,d]
    marinalist += [templ]
    print(marinalist,)
for row in marinalist:
    print(row)
