def solution(n):
    answer = ''
    start = n
    
    while True:
        
        if start%3 == 0:
            answer+='4'
            start=start//3-1
        
        elif start%3 == 1:
            answer+='1'
            start=start//3
            
        else:
            answer+='2'
            start=start//3
            
        
        if n<4:break
            
        
        if start<4:
            if start%3 == 0:
                answer+='4'
        
            elif start%3 == 1:
                answer+='1'
            
            else:
                answer+='2'
            break
        
    
    
    return answer[::-1]