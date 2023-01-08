S, P = map(int, input().split())
DNA_org = list(input())
tmp = list(map(int, input().split()))
ans_dic = {'A': tmp[0], 'C': tmp[1], 'G': tmp[2], 'T': tmp[3]}
chk_dic = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

answer = 0

for i in range(S-P+1):
    flag = True

    if i == 0:
        for j in range(P):
            chk_dic[DNA_org[j]] += 1
    else:
        chk_dic[DNA_org[i+P-1]] += 1
        chk_dic[DNA_org[i-1]] -= 1

    for i in ('A', 'C', 'G', 'T'):
        if chk_dic[i] < ans_dic[i]:
            flag = False
            break

    if flag:
        answer += 1

print(answer)