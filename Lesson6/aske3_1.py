N = 112

if N == 0:
    print("It's not prime")
elif N == 1:
    print("It's not prime")
else:
    for i in range(2,N):
        if N % i == 0:
            print("It's not prime")
            break
    else:
        print("It's prime")