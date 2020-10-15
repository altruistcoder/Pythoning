n = int(input("Enter a number: "))
for i in range(n, 0, -1):
    for j in range(1, 2*n):
        if j <= n-i:
            print(" ", end="")
        elif j < n+i:
            if j <= n:
                print(chr(64+j), end="")
            else:
                print(chr(64+2*n-j), end="")
    print()
