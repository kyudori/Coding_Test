import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr_sum = [0]
sum = 0

# 합 배열
for i in range(N) :
    sum += arr[i]
    arr_sum.append(sum)

# 구간 합
for _ in range(M) :
    start, end = map(int, input().split())
    print(arr_sum[end] - arr_sum[start - 1])

    #https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline
    