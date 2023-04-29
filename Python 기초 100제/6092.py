n = int(input())

result = [0]*23
number = list(map(int, input().split()))

for i in range(n):
    result[number[i]-1] += 1

for i in range(23):
    print(result[i], end = ' ')
