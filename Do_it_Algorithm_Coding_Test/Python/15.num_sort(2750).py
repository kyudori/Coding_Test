N = int(input())
A=[]

for _ in range(N):
    A.append(int(input()))

for i in range(N-1):
    for j in range(N-1-i):
        if A[j] > A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]

for i in range(N):
    print(A[i])