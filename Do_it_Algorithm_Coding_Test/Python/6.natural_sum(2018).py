N = int(input())

sum = 1
count = 1
start_index = 1
end_index = 1

while end_index != N :
    if (sum > N) :
        sum = sum - start_index
        start_index += 1
    elif (sum < N) :
        end_index += 1
        sum = sum + end_index
    else :
        end_index += 1
        sum = sum + end_index
        count += 1

print(count)