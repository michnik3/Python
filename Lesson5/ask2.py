cnt = 1
sum = 0
while cnt <= 10:
    user_input = input("Give " + str(cnt) + "th number")
    sum = sum + int(user_input)
    print(sum)
    cnt += 1