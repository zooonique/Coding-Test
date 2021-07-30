from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()    
    que = deque(people)
    
    while que:
        # 가장 몸무게가 적은 사람의 두 배가 limit을 초과하면 같이 태우기는 불가능
        if que[0]*2 >limit:
            answer+=len(que)
            break
        
        
        # 몸무게가 가장 적은 사람 + 몸무게가 가장 큰 사람 <= limit
        if que[0] + que[-1] <= limit and len(que)>1:
            que.popleft()
            que.pop()
            
        else:
            que.pop()
            
        answer+=1

    return answer
