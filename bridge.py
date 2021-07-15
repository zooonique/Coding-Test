from collections import deque

def solution(limit, weight, trucks):
    
    answer = 0
    
    bridge = deque([0]*limit)
    trucks = deque(trucks)
    
    SUM = 0
    
    
    while trucks:
        
        # 퇴장
        SUM-=bridge.pop()
            
        # 진입
        if limit > len(bridge) and weight >= SUM + trucks[0]: # sum O(N)이 시간이 오래 걸려서 해당 방법으로 해결
            bridge.appendleft(trucks.popleft())
            SUM+=bridge[0]
            
        else:
            bridge.appendleft(0)
        
        answer+=1
        
    answer+=limit
        
    return answer