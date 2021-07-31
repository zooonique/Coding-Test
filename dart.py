def solution(dartResult):
    answer = 0
    shot = 0
    bonus = ['S','D','T']
    options = ['*','#']
    point = []
    p=''
    
    for i in dartResult:
        # 숫자
        if i not in options and i not in bonus:
            p+=i
        
        # 숫자가 아닌 경우
        else:
            # 옵션일 경우
            
            if i == '*':
                
                # 1 샷에서 * 옵션일 경우 해당 점수에 2배
                if shot == 1:
                    point[0] = point[0]*2 
                
                # 2,3 샷에서 * 옵션일 경우 앞에 이전 점수와 지금 점수에 2배
                else:
                    point[shot-2]*=2
                    point[shot-1]*=2
                    
            # '#' 옵션
            if i == '#':
                point[shot-1]*=-1
            
            
            # 점수가 존재하고 보너스인 경우
            if p:
                p = int(p)
                shot += 1
                
                if i in bonus:
                    if i == 'S':
                        p=p**1
                    
                    elif i == 'D':
                        p=p**2
                        
                    else:
                        p=p**3
                
                point.append(int(p))
                
                
            p=''
    
    return sum(point)
