
print("==============================")

N = 5
A = set()
for i in range(1, N+1):
    A.add(i)

print(A)

result = set()
for element in A:
    my_tuple = (element, element ** 2)
    result.add(my_tuple)

print(result)