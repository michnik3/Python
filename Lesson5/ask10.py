bf = ["a", "b", "c"]
party_friends = ["1", "2", "a", "4", "5", "6", "b", "8", "9", "10"]
cnt = 0

for friend in bf:
    if bf in party_friends:
        cnt += 1
if cnt < 2:
    print("I don't go")
else:
    print("I'll come")
