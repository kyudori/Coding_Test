# https://redcow77.tistory.com/360
# https://infinitt.tistory.com/229
# https://wikidocs.net/15

import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    arr.append((int(input()),i))

sorted_arr = sorted(arr) 
answer = [] 

for i in range(N):
    answer.append(sorted_arr[i][1] - arr[i][1])

print(max(answer) + 1)