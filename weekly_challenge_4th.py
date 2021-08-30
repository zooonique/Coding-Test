def solution(table, languages, preference):
    answer = ''
    
    t = [0,5,4,3,2,1]
    job = []
    point = []
    
    table.sort()
    for i in table:
        job.append(i.split())
    
    for j in job:
        tmp = []
        for l in range(len(languages)):
            if languages[l] in j:
                tmp.append(preference[l]*(t[j.index(languages[l])]))
                
            else:
                continue
        
        point.append(sum(tmp))
        
    
    
    return job[point.index(max(point))][0]
