h, w = map(int, input().split())
board = [[0 for _ in range(w)] for _ in range(h)]


n = int(input())

for _ in range(n):
    l, d, x, y = map(int, input().split())

    if d == 0: #0->가로
        for _ in range(l):
            board[x-1][y-1] = 1
            y += 1
    else:
        for _ in range(l):
            board[x-1][y-1] = 1
            x += 1

for i in range(h):
    for j in range(w):
        print(board[i][j], end = ' ')

    print()

