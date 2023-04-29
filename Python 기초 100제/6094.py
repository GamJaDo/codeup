n = int(input())
number = list(map(int, input().split()))

min_number = n

for i in range(n):
    if number[i] < min_number:
        min_number = number[i]
        
print(min_number)
