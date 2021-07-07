def solution(prices):
    answer = []
    
    for start in range(len(prices)):
        day = 0
        for end in range(start+1,len(prices)):
            if prices[start] > prices[end]:
                day+=1
                break
                
            else:
                day+=1
        
        answer.append(day)
    
    
    return answer