import sys
input = sys.stdin.readline()

N = int(input())
array = [0] * 100001

for i in input().split():
    array[int(i)] = 1

M = int(input())
x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')