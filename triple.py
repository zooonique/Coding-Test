def solution(n):
    answer = 0
    triple = ''
    
    while n>=3:
        triple += str(n%3)
        n=n//3
    triple += str(n)
    triple = triple[::-1]
    
    for i in range(len(triple)):
        answer+=int(triple[i])*(3**i)
    
    
    return answer