import sys
print = sys.stdout.write
A = list(input())

for i in range(len(A)):
    Max_idx = i
    for j in range(i+1, len(A)):
        if A[j] > A[Max_idx]:
            Max_idx = j
    if A[i] < A[Max_idx]:
        A[i], A[Max_idx] = A[Max_idx], A[i]

for i in range(len(A)):
    print(A[i])