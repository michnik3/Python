day = "Sunday"
tired =True

if day == "Saturday":
    print("i read a bit")
elif day == "Sunday":
    if tired:
        print("i won't study at all")
    else:
        print("I will study a lot")
else:
    print("I will study")
