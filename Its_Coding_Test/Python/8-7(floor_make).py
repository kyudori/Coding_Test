import sys
input = sys.stdin.readline
n = int(input())

d = [0] * (n + 1)
def bottom(x):
	d[1] = 1
	d[2] = 3
	
	if d[x] != 0:
		return d[x]
        
	d[x] = bottom(x - 1) + (bottom(x - 2) * 2)
	return d[x]
    
print(bottom(n) % 796796)

# import sys
# input = sys.stdin.readline

# n = int(input())


# d = [0] * (n + 1)

# # 타일 길이가 1, 2 일 때 값 설정
# d[1] = 1
# d[2] = 3

# for x in range(3, n + 1):
# 	d[x] = d[x - 1] + (d[x - 2] * 2)
    
# print(d[n] % 796796)