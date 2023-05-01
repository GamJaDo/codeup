n = int(input())

solution = list(map(int, input().split()))

solution.sort()

standard = 2000000001
left_point = 0
right_point = len(solution)-1
result = []

while left_point < right_point:
    solution_sum = solution[left_point] + solution[right_point]

    if abs(solution_sum) < standard:
        result = [solution[left_point], solution[right_point]]

        standard = abs(solution_sum)

    if solution_sum < 0:
        left_point += 1
    else:
        right_point -= 1

print(result[0], result[1])
