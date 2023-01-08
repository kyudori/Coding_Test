import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = list(map(int, input().split()))
s.sort()
print(s[k - 1])

# import sys
# input = sys.stdin.readline
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

# def quickSort(S, E, K):
#     global A
#     if S < E:
#         pivot = partition(S, E)
#         if pivot == K:  # K번째 수가 pivot이면 더이상 구할 필요 없음
#             return
#         elif K < pivot:  # K가 pivot보다 작으면 왼쪽 그룹만 정렬
#             quickSort(S, pivot - 1, K)
#         else:  # K가 pivot보다 크면 오른쪽 그룹만 정렬
#             quickSort(pivot + 1, E, K)


# def swap(i, j):
#     global A
#     A[i], A[j] = A[j], A[i]


# def partition(S, E):
#     global A
#     if S + 1 == E:
#         if A[S] > A[E]:
#             swap(S, E)
#         return E

#     M = (S + E) // 2
#     swap(S, M)
#     pivot = A[S]
#     i = S + 1
#     j = E
#     while i <= j:
#         while pivot < A[j] and j > 0:
#             j = j - 1
#         while pivot > A[i] and i < len(A)-1:
#             i = i + 1
#         if i <= j:
#             swap(i, j)
#             i = i + 1
#             j = j - 1
#     # i == j 피벗의 값을 양쪽으로 분리한 가운데에 오도록 설정하기
#     A[S] = A[j]
#     A[j] = pivot
#     return j


# quickSort(0, N - 1, K - 1)
# print(A[K - 1])

# ===============

# def merge_sort(array):
#     if len(array)<=1:
#         return array
#     mid = len(array) // 2
#     left = merge_sort(array[:mid])
#     right = merge_sort(array[mid:])

#     i,j,k = 0,0,0

#     while i < len(left) and j <len(right):
#         if left[i] < right[j]:
#             array[k] = left[i]
#             i += 1
#         else:
#             array[k] = right[j]
#             j += 1
#         k+=1
    
#     if i==len(left):
#         while j < len(right):
#             array[k] = right[j]
#             j += 1
#             k += 1
#     elif j==len(right):
#         while i < len(left):
#             array[k] = left[i]
#             i += 1
#             k += 1
#     return array

# # 데이터 입력
# n,k = map(int,input().split())

# num = list(map(int, input().split()))
# num = merge_sort(num)

# print(num[k-1])

# ==================

# N,K=map(int,input().split())
# l=list(map(int,input().split()))
# if K==1:
#     print(min(l))
# elif K==N:
#     print(max(l))
# else:
#     l.sort()
#     print(l[K-1])