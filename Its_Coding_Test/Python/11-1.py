import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))

data.sort()

group_n = 0
member_n = 0


for x in data:
    member_n += 1
    if(member_n >= x):
        group_n += 1
        member_n = 0
    
print(group_n)