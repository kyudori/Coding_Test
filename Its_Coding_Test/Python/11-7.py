string = list(map(int, input()))
mid = len(string)//2
sum1 = 0
sum2 = 0

for i in range(mid):
    sum1 += string[i]
    sum2 += string[i+mid]

if sum1 == sum2:
    print("LUCKY")
else :
    print("READY")