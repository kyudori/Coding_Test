N = int(input())

score = list(map(int,input().split()))
sum = 0

for i in range(0, N):
    sum = sum + score[i]

max_score = 0

for j in range(0, N):
    if(max_score < score[j]):
        max_score = score[j]

print(sum/max_score*100/N)
