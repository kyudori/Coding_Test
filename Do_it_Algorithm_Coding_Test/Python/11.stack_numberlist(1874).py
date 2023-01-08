n = int(input())

num = 1
stack = []
answer = []

for _ in range(n):
    data = int(input())

    while num <= data:
        stack.append(num)
        answer.append('+')
        num += 1

    if stack.pop() == data:
        answer.append('-')

    else:
        print("NO")
        exit(0)

print("\n".join(answer))
# https://blockdmask.tistory.com/468

# N = int(input())

# A = [0]*N
# for i in range(N):
#     A[i] = int(input())

# stack = []
# num = 1
# answer = True
# answer = ""

# for i in range(N):
    
#     cur = A[i]
    
#     if cur >= num:   
#         while cur >= num:
#             stack.append(num)
#             num += 1
#             answer += "+\n"
#         stack.pop()
#         answer += "-\n"
    
#     else:          
#         top_num = stack.pop()
#         if top_num > cur: 
#             print("NO")
#             answer = False
#             break
#         else:
#             answer += "-\n"

# if answer:
#     print(answer)