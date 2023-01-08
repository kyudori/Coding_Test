import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))
arr.sort()

answer = 0

for k in range(N):
    find = arr[k]
    start_index = int(0)
    end_index = int(N - 1)
    while start_index < end_index:
        if arr[start_index] + arr[end_index] == find:
            if start_index != k and end_index != k:
                answer += 1
                break
            elif start_index == k:
                start_index += 1
            elif end_index == k:
                end_index -= 1
        elif arr[start_index] + arr[end_index] < find:
            start_index += 1
        else:
            end_index -= 1
print(answer)