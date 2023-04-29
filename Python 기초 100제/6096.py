board = [0]*19

for i in range(19):
    board[i] = list(map(int, input().split()))


n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    for j in range(19):
        if board[j][y-1] == 1:
            board[j][y-1] = 0
        else:
            board[j][y-1] = 1

        if board[x-1][j] == 1:
            board[x-1][j] = 0
        else:
            board[x-1][j] = 1


for i in range(19):
    for j in range(19):
        print(board[i][j], end = ' ')

    print()
