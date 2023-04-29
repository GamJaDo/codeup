n = int(input())
number = list(map(int, input().split()))

for i in number[::-1]:
    print(i, end = ' ')
