import sys
input= sys.stdin.readline

def binary_search(array, start, end):
    res = 0
    while start <= end:
        mid = (start+end) // 2
        total = 0
        
        for x in array:
            if x > mid:
                total+= x- mid
            
        if total < m:
            end = mid-1

        else:
            result = mid
            start = mid +1

    return result
        
n , m = map(int,input().split())
array = list(map(int,input().split()))

result = binary_search(array, 0, max(array))
print(result)


# N, M = list(map(int, input().split(' ')))
# array = list(map(int, input().split()))

# start = 0
# end = max(array)

# result = 0

# while(start < end):
#     total = 0
#     mid = (start+end)//2
#     for x in array:
#         if x > mid:
#             total += x - mid
#     if total < M:
#         end = mid - 1
#     else:
#         result = mid
#         start = mid + 1

# print(result)