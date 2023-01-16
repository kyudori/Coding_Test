import sys
#input = sys.stdin.readline()
#왜 에러가 날까

N = int(input())
array = list(map(int, input().split()))

M = int(input())
x = list(map(int, input().split()))

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)
    
for i in x:
    result = binary_search(array, i, 0, N-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')