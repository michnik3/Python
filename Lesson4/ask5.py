cash_desk = []
cash_desk.insert(0 , "Tom")
cash_desk.insert(1, "Bob")
print(cash_desk)
cash_desk.remove("Tom")
print("served")
print(cash_desk)
cash_desk.insert(1, "Pam")
cash_desk.insert(2, "Jim")
print(cash_desk)
cash_desk.remove("Bob")
print("served")
print(cash_desk)

print("------------------")
print("2os tropos pio swstos")
print("------------------")

cash_desk = []
cash_desk.append("Tom")
cash_desk.append("Bob")
print(cash_desk)
person = cash_desk.pop(0)
print(person + " served")
cash_desk.append("Pam")
cash_desk.append("Jim")
print(cash_desk)
person = cash_desk.pop(0)
print(person + " served")
print(cash_desk)