from collections import deque

def solution(n, words):
    answer = []
    words = deque(words)
    past = deque([])
    
    while words:
        if not past:
            past.append(words.popleft())
            continue
        
        if past[-1][-1]!=words[0][0]:
            return len(past)%n+1,len(past)//n+1
            
        else:
            if words[0]  not in past:
                past.append(words.popleft())
                
            else:
                return len(past)%n+1,len(past)//n+1
    
    return 0,0
