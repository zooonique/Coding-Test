def solution(s):
    answer = ''
    text =list(s.split(' '))
    
    for i in text:
        answer+=i.lower().capitalize()+' '
    
    return answer[:-1]
