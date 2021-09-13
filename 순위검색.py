def solution(info, query):
    answer = []
    members = []
    orders = []

    for i in info:
        members.append(list(i.split()))
    
    for i in query:
        orders.append(list(i.split(' ')))
    
    
    for i in orders:
        while True:
            if 'and' not in i:
                break
            else:
                i.remove('and')
            
    for i in orders:
        cnt = 0
        for j in members:
            chk = 0
            for k in range(5):
                if k == 4 and int(i[k]) <= int(j[k]):
                    cnt+=1
                    break    
                
                if i[k] == '-':
                    chk+=1
                    
                elif i[k] == j[k]:
                    chk+=1
                    
                else:
                    break
        answer.append(cnt)
            
    return answer
