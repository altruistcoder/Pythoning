n = int(input("Enter a number: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        if j==1 or j == i:
            print(i, end="\t")
        else:
            print(0, end="\t")
    print(end="\b\n")

