def solution(s):
    answer = ''
    x=list(s)
    x.sort()
    for i in x[::-1]:
        answer+=i
    
    return answer
