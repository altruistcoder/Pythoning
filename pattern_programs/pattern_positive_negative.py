n = int(input("Enter length of array: "))
a = list(map(int, input("Enter the array: ").split()))
m = 0
for i in a:
    if abs(i) > m:
        m = abs(i)
a2 = []
for i in range(n):
    l = ""*m
    a2.append(l)

print(a2)

for i in range(1, 2*n):
    if n % 2 != 0:
        x = ""*(2*m+1)
