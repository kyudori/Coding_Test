import sys

n = int(sys.stdin.readline().rstrip())
n_list = list(map(int,sys.stdin.readline().rstrip().split()))

dp_table = [0] * 100

dp_table[0] = n_list[0]
dp_table[1] = max(n_list[0], n_list[1])
for i in range(2, n):
    dp_table[i] = max(n_list[i-1], n_list[i-2] + n_list[i])

print(dp_table[n-1])