from collections import deque
# https://dongdongfather.tistory.com/72

N = int(input())
dq = deque()

for i in range(1,N+1):
    dq.append(i)

while len(dq) > 1:
    dq.popleft()
    dq.append(dq.popleft())

print(dq[0])