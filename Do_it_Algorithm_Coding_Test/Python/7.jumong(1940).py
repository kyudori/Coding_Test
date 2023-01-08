import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

material = list(map(int, input().split()))

material.sort()
# for i in range(1, len(material)) : 
#     while (i>0) & (material[i] < material[i-1]) :
#         material[i], material[i-1] = material[i-1], material[i]
#         i -= 1
# 내가 구현해서 쓰면 Error남

count = 0
start_index = 0
end_index = N-1

while start_index < end_index :
    if material[start_index] + material[end_index] < M:
        start_index += 1
    elif material[start_index] + material[end_index] > M:
        end_index -= 1
    else:
        count+=1
        start_index+=1
        end_index-=1

print(count)