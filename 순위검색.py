from itertools import combinations

def solution(info, query):
    answer = []
    members = {}
    orders = []
    
    
    for i in info:
        m = i.split()
        # info의 score를 따로 저장
        score = int(m[-1])
        m = m[:4:]
        # info 1개를 16개의 경우의 수로 분리
        for n in range(5):
            for c in combinations(m,n):
                key = ''
                for i in list(c):
                    key += i
                
                # dict에 key값은 공백 불가
                if key=='':
                    key='----'
                
                # 이미 dict에 있는 key값이라면 score를 추가
                if key in members:
                    members[key].append(score)
                    
                # 없는 key값이라면 사전에 key와 value 생성
                else:
                    members[key] = [score]
    
    # dict안에 value(score)를 정렬
    for key in members:
        members[key]=sorted(members[key])
    
    
    for q in query:
        # 쿼리 파싱 (and, - 제거)
        q = q.replace(" and ", "").replace("-", "")
        order , score = q.split(" ")
        score = int(score)
        
        if order == '':
            order = '----'
        
        
        man = 0
        # order이 key값이 된다.
        # order이 members dict안에 key로 존재하면,
        if order in members:
            start, end = 0, len(members[order])
            # 이진탐색
            while start<end:
        
                mid = (start+end)//2        
                if members[order][mid] >= score:
                    end = mid
                
                else:
                    start = mid +1
                    
            man = len(members[order])-start
            
        answer.append(man)
    
    return answer
