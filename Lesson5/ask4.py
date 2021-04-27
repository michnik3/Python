l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cnt = 1
max = l1[0]
while cnt < len(l1):
    if l1[cnt] > max:
        max = l1[cnt]
    cnt += 1

print(max)
