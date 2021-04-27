primes_list = []

for N in range(2,100+1):
    for i in range(2,N):
        if N % i == 0:
            break
    else:
        print("It's prime")

primes = tuple(primes_list)
print(primes)