# # 1st Method:
#
#
# from math import sqrt
#
#
# def prime(n):
#     for i in range(2, int(sqrt(n))+1):
#         if n % i == 0:
#             return False
#     return True
#
#
# for _ in range(int(input("Enter no. of test cases: "))):
#     m, n = map(int, input("Enter two numbers: ").split())
#     for i in range(m, n+1):
#         if i == 1 or (i % 2 == 0 and i != 2):
#             continue
#         elif prime(i):
#             print(i, end=" ")
#     print()


# # 2nd Method:


# from math import sqrt
#
#
# def prime(n):
#     for i in range(2, int(sqrt(n))+1):
#         if n % i == 0:
#             return False
#     return True
#
#
# for _ in range(int(input("Enter no. of test cases: "))):
#     m, n = map(int, input("Enter two numbers: ").split())
#     if m % 2 != 0:
#         for i in range(m, n+1, 2):
#             if i == 1:
#                 continue
#             elif prime(i):
#                 print(i, end=" ")
#     else:
#         if m == 2:
#             print(2, end=" ")
#         for i in range(m+1, n+1, 2):
#             if i == 1:
#                 continue
#             elif prime(i):
#                 print(i, end=" ")
#     print()


# # 3rd Method (Sieve's Method):


for _ in range(int(input("Enter no. of test cases: "))):
    m, n = map(int, input("Enter two numbers: ").split())
    if m == 1:
        m += 1
    if m % 2 != 0:
        sieve = [True] * (n-m+2)
        for p in range(m, n+1, 2):
            if sieve[p-m]:
                print(p, end=" ")
            for i in range(p, n+1, p):
                sieve[i-m] = False
    else:
        if m == 2:
            print(2, end=" ")
        m += 1
        sieve = [True] * (n - m + 2)
        for p in range(m, n + 1, 2):
            if sieve[p - m]:
                print(p, end=" ")
            for i in range(p, n + 1, p):
                sieve[i - m] = False
    print()
