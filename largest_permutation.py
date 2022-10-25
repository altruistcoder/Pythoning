n, k = map(int, input().strip().split(' '))
arr = list(map(int, input().strip().split(' ')))
for i in range(k):
    m = max(arr[i:])
    p = arr.index(m)
    arr[i], arr[p] = arr[p], arr[i]
print(" ".join(map(str, arr)))
