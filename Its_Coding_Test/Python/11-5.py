# import sys
# input = sys.stdin.readline

# N, M = map(int,input().split())
# B = list(map(int,input().split()))

# count = 0

# for i in range(0,n):
#   for j in range(i+1,n):
#     if B[i] != B[j]:
#       count += 1

# print(count)



import sys
input = sys.stdin.readline

N, M = map(int, input().split())
B = list(map(int, input().split()))

count = 0
weight = [0] * (M+1)

for x in B:
    weight[x] += 1

for i in range(1, M+1):
    N -= weight[i]
    count += weight[i] * N

print(count)