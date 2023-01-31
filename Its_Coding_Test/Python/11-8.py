S = list(input())
S.sort()

A = []
sum = 0

for i in range(len(S)):
    if 'Z'>=S[i]>='A':
        A.append(S[i])
    else:
        sum += int(S[i])

A.append(str(sum))

for j in range(len(A)):
    print(A[j], end='')