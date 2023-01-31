import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
K = int(input())

arr = [[0] * (N+1) for _ in range(N+1)]
for _ in range(K):
    x, y = map(int, input().split())
    arr[x][y] = 1

# 방향전환 횟수
L = int(input())
time_dic = {}
for i in range(L):
    X, C = input().split()
    time_dic[int(X)] = C

# 우하좌상
dx = [0, 1, 0, -1]  # 행
dy = [1, 0, -1, 0]  # 열

# 뱀 초기위치, 방향 초기
x, y, d = 1, 1, 0

# 뱀
snake = deque([])
time = 0
while True:
    # 뱀머리 현재 위치
    snake.append((x, y))
    time += 1

    x += dx[d]
    y += dy[d]
    # 벽에 부딪히거나 자기 몸과 부딪히면
    if x < 1 or x >= (N+1) or y < 1 or y >= (N+1) or arr[x][y] == 2:
        break
    # 벽이 아니면
    # 사과가 없다면
    if not arr[x][y]:
        # 꼬리 없애주고
        i, j = snake.popleft()
        arr[i][j] = 0

    arr[x][y] = 2

    # 머리 이동
    if time in time_dic:
        if time_dic[time] == 'D':
            d = (d + 1) % 4
        else:
            d = (d - 1) % 4

print(time)