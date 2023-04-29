board = [0]*10
for i in range(10):
    board[i] = list(map(int, input().split()))
x, y = 1, 1

if board[x][y] != 2:
    board[x][y] = 9

while True:
    if board[x][y] == 2:
        board[x][y] = 9
        break

    if board[x][y+1]==0 or board[x][y+1]==2:
        board[x][y] = 9
        y += 1
    elif board[x+1][y]==0 or board[x+1][y]==2:
        board[x][y] = 9
        x += 1

    if x==8 and y==8:
        board[x][y] = 9
        break

for i in range(10):
    for j in range(10):
        print(board[i][j], end = ' ')

    print()
