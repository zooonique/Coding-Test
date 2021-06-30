# dict형도 쓸 곳이 있다,
def solution(record):
    answer = []
    slice_record = []
    user = {}
    for i in record:
        slice_record.append(i.split())
        
        
    for i in slice_record:
        if len(i) == 3:
            user[i[1]]=i[2]
    
    
    for i in slice_record:
        if i[0] == 'Enter':
            answer.append(user[i[1]]+'님이 들어왔습니다.')
            
        elif i[0] == 'Leave':
            answer.append(user[i[1]]+'님이 나갔습니다.')
            
    
    return answer