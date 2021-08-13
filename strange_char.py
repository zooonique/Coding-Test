def solution(s):
    answer = ''
    # 짝수 대문자, 홀수 소문자
    
    idx = 0
    for i in s:
        if i == ' ':
            idx=0
            answer+=i
            continue
        
        if idx%2==0:
            answer+=i.upper()
            
        else:
            answer+=i.lower()
            
        idx+=1
    
    
    return answer
