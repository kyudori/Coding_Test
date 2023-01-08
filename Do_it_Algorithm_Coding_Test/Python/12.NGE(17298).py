import sys
n = int(input())
A = list(map(int, input().split()))
answer = [-1] * n
stack = []

stack.append(0)
for i in range(1, n):
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)

result = ""

for i in range(n):
    result += str(answer[i])+" "
print(result)

#print(*answer) 해도 됨