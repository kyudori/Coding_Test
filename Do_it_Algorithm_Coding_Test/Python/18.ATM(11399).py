N = int(input())
T = list(map(int, input().split()))
time = 0
T.sort()
for i in range(N):
    for j in range(i + 1):
        time += T[j]
print(time)