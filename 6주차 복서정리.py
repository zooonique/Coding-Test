def solution(weights, head2head):
    answer = []
    size = len(weights)
    rank = []
    
    heavy = [0]*size
    win = [0]*size
    
    for i in range(size):
        match = size
        for j in range(size):
            
            if head2head[i][j] == 'N':
                match -= 1
                continue
            
            if head2head[i][j] == 'W':
                win[i] += 1
                if weights[i] < weights[j]:
                    heavy[i] += 1
                    
        if match != 0:
            win[i] = win[i] / match
            
        else:
            win[i] = 0
        
    for i in range(size):
        rank.append([win[i],heavy[i],weights[i],-(i+1)])
    
    rank.sort()
    rank.reverse()
    
    for i in rank:
        answer.append(abs(i[3]))
        
    return answer
