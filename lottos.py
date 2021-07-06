def solution(lottos, win_nums):
    answer = []
    best = []
    worst = []
    bingo = [6,6,5,4,3,2,1]
    
    for i in lottos:
        if i in win_nums:
            best.append(True)
            worst.append(True)
            
        else:
            if i == 0:
                best.append(True)
            else:
                best.append(False)
                
            worst.append(False)
    
    
    answer.append(bingo[best.count(True)])
    answer.append(bingo[worst.count(True)])
    
    
    return answer