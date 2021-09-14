def solution(word):
    answer,step = 0,0
    alp = ['A', 'E', 'I', 'O', 'U']
    
    arr = []
    
    for i in range(5):
        step+=5**i
        arr.append(step)
    arr.reverse()
    
    num = ''
    for i in word:
        num+=str(alp.index(i))
        
        
    for i in range(len(num)):
        answer+=int(num[i])*arr[i]
    
    answer+=len(num)
    
    
    return answer
