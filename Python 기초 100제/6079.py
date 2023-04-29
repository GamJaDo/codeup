n = int(input())
i = 0

result = 0

while True:
    if result >= n:
        print(i)
        break

    i += 1
    result += i
