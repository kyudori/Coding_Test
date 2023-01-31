def solution(s):
    
    answer = len(s)
    
    for i in range(1, int(len(s)/2) + 1):
        position = 0
        len_add = len(s)
        
        while position + i <= len(s):
            unit_s = s[position:position+i]
            position += i
            
            count = 0
            
            while position + i <= len(s):
                if unit_s == s[position:position+i]:
                    count += 1
                    position += i
                
                else:
                    break
                    
            if count > 0:
                len_add -= i * count
                
                if count < 9:
                    len_add += 1 
                    
                elif count < 99:
                    len_add += 2
                    
                elif count < 999:
                    len_add += 3
                    
                else:
                    len_add += 4
                    
        answer = min(answer, len_add)
                
    return answer