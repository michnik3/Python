x = int(input("Dwse arithmo metaxi tou 3 kai tou 20: "))
flag = True
while flag == True :
    if x >= 3 and x <= 20:
        print("correct! ")
        flag = False
    else:
        print("lathos arithmos. ")
        x = int(input("Dwse arithmo metaxi tou 3 kai tou 20: "))

print("===========================")

N = int(input("Give N: "))
while N < 3 or N > 20:
    N = int(input("Give N(3 - 20): "))

numbers = []
for cnt in range(0,N):
    numbers.append(int(input("Give "+ str(cnt + 1) + "th number: ")))

print(numbers)

numbers.sort()
print(numbers)