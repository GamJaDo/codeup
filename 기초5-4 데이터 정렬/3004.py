def binary_search(arr, t, low, high):
    while low <= high:
        middle = (low+high)//2
        if t == arr[middle]:
            return middle
        elif t > arr[middle]:
            low = middle + 1
        else:
            high = middle - 1

    return None

n = int(input())

arr = list(map(int, input().split()))

sort_arr = sorted(arr)

for i in range(n):
    print(binary_search(sort_arr, arr[i], 0, n-1), end = ' ')
