x1 = int(input("Dwse x1: "))
x2 = int(input("Dwse x2: "))

y1 = int(input("Dwse y1: "))
y2 = int(input("Dwse y2: "))

sumx = x1 + x2
sumy = y1 + y2

if sumx > sumy:
    print("paizei o paxtis x")
elif sumx == sumy:
    print("draw")
else:
    print("paizei o paixtis y")