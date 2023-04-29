n = input()
temp = 97

while True:
    if temp >= (ord(n)+1):
        break
    else:
        print(chr(temp), end = ' ')
        temp += 1

