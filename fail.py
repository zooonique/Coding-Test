def solution(N, stages):
    answer = []
    fail = []
    tmp = []
    
    # 각 스테이지에 실패한 사람
    
    for i in range(N+1):
        fail.append(0)
        
    for i in stages:
        fail[i-1]+=1
        
    rev_fail = list(reversed(fail))
    
    for i in range(len(fail)-1):
        if sum(rev_fail)==0:
            tmp.append(0)
            
        else:
            tmp.append(fail[i]/sum(rev_fail))
        rev_fail.pop()
    
    
    
    for i in range(len(tmp)):
        m=tmp.index(max(tmp))
        answer.append(m+1)
        tmp[m]=-1
    
            
        
    return answer