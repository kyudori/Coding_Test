import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

first = data[N-1]
second = data[N-2]

count = M // (K+1) * K + M % (K+1)

# count = M // (K+1) * K
# count += M % (K+1)

result = 0
result += (count) * first
result += (M-count) * second

print(result)