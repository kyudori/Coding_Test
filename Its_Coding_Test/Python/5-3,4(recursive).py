def recursive_func(i):
    if i == 100:
        return
    print(i, '번째 재귀 함수에서', i+1, '번째 재귀 함수 호출')
    recursive_func(i+1)
    print(i, '번째 재귀 함수 종료')

recursive_func(1)