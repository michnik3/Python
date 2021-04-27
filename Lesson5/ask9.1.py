hidden_number = 33
guess = int(input("Dwse arithmo: "))
max_tries = 4
cnt = 0
if guess == hidden_number:
    print("You win!")
while guess != hidden_number:
    cnt += 1
    if cnt == max_tries:
        print("You've Lost!")
        break
    if guess > hidden_number:
        print("Edwses megalitero arithmo")
        guess = int(input("Dwse pali arithmo: "))

    elif guess < hidden_number:
        print("Edwses mikrotero arithmo")
        guess = int(input("Dwse pali arithmo: "))
    else:
        print("Success! ")
        break

print("=================================")
