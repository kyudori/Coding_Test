import sys
input = sys.stdin.readline

N = int(input())
money = list(map(int, input().split()))
money.sort()
answer = 1

for m in money:
    if m > answer:
        break
    else:
        answer += m

print(answer)