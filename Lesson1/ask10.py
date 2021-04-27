hours = int(input("Dwse to pli8os wrwn: "))
minutes = int(input("Dwse to pli8os leptwn: "))
seconds = int(input("Dwse to pli8os deyteroleptwn: "))


if hours < 10:
    message1 = "0" + str(hours)
else:
    message1 = str(hours)

if minutes < 10:
    message2 = "0" + str(minutes)
else:
    message2 = str(minutes)

if seconds < 10:
    message3 = "0" + str(seconds)
else:
    message3 = str(seconds)

message = message1 +" : " +  message2 + " : " + message3

print (message)

