def solution(s, n):
    answer = ''
    
    for i in s:
        if i == ' ':
            answer+=i
            continue
            
        else:
            if ord(i)+n > ord('z') and ord(i) >= ord('a'):
                answer+=chr(ord('a')+ord(i)+n-ord('z')-1)
                
            elif ord(i)+n > ord('Z') and ord(i) < ord('a'):
                answer+=chr(ord('A')+ord(i)+n-ord('Z')-1)
                
            else:
                answer+=chr(ord(i)+n)
            
        
    
    
    return answer