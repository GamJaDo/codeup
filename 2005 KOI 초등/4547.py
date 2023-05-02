n = int(input())

max_location = 0
max_height = 0

data = [0]*1001
for i in range(n):
    location, height = map(int, input().split())
    data[location] = height
    
    if max_height < height:
        max_height = height
        max_location = location
"""
left = [0]*max_location
right = [0]*(max_location*2)
"""
left = [0]*1001
right = [0]*1001

for i in range(1001):
    if data[i]==0:
        continue
    if i < max_location:
        left[i] = data[i]
    else:
        right[i] = data[i]
limit = 0
result = 0

right.reverse()
for i in range(max_location):
    if limit < left[i]:
        limit = left[i]
    
    result += limit

limit = 0    
for i in range(len(right)):
    if right[i] == max_height:
        break
    if limit < right[i]:
        limit = right[i]
    
    result += limit

print(result+max_height)

