def solution(numbers, hand):
    answer = ''
    center = [2,5,8,0]
    distance = [0,0]
    lh = -1
    rh = 1
    
    for i in numbers:
        if i == 1 or i == 4 or i ==7:
            answer+="L"
            lh = i
            
        elif i == 3 or i == 6 or i == 9:
            answer+="R"
            rh = i
        
        else:
            idx = center.index(i)
            
            if lh in center and rh in center:
                lh_idx = center.index(lh)
                rh_idx = center.index(rh)
                
            
            elif lh in center and rh not in center:
                lh_idx = center.index(lh)
                rh_idx = center.index(rh-1)
                distance[1] = 1
                
            elif lh not in center and rh in center:
                lh_idx = center.index(lh+1)
                rh_idx = center.index(rh)
                distance[0] = 1
                
            else:
                lh_idx = center.index(lh+1)
                rh_idx = center.index(rh-1)
                distance = [1,1]
                
            
            if abs(idx-lh_idx)+distance[0] > abs(idx-rh_idx)+distance[1]:
                answer+="R"
                rh=i
                
            elif abs(idx-lh_idx) + distance[0] < abs(idx-rh_idx) + distance[1]:
                answer+="L"
                lh=i
            
            else:
                if hand=='right':
                    answer+="R"
                    rh=i
                
                else:
                    answer+="L"
                    lh=i
            
            distance = [0,0]
            
    
    return answer