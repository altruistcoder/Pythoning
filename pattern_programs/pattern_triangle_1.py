n = int(input("Enter a number: "))
for i in range(1, n+1):
    for j in range(1, 2*i):
        if j % 2 == 1:
            print(i, end="")
        else:
            print("*", end="")
    print()

for i in range(n-1, 0, -1):
    for j in range(1, 2*i):
        if j % 2 == 1:
            print(i, end="")
        else:
            print("*", end="")
    print()

# Alternate Solution:

n = int(input("Enter a number: "))
# for i in range(1, 2*n):
#     if i <= n:
#         for j in range(1, 2*i):
#             if j % 2 == 1:
#                 print(i, end="")
#             else:
#                 print("*", end="")
#         print()
#     else:
#         for j in range(1, 2*(2*n-i)):
#             if j % 2 == 1:
#                 print(2*n-i, end="")
#             else:
#                 print("*", end="")
#         print()
