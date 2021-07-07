def step_2(new_id):
    items = ['-','_','.']
    for i in new_id:
        if i.islower()==True or i.isdigit() == True or i in items:
            continue
            
        else:
            new_id = new_id.replace(i,'')
            
    return new_id


def step_3(new_id):
    if '..' in new_id :
        new_id = new_id.replace('..','.')
        return step_3(new_id)
        
    else:
        return new_id
    
def step_4(new_id):
    
    if len(new_id) == 1 and new_id[0] == '.':
        return ''
    
    if new_id[-1] == '.':
        print(new_id)
        new_id = new_id[:len(new_id)-1:]
    
    if new_id[0] == '.':
        new_id = new_id[1::]
    
    return new_id

def step_7(new_id,length):
    if length>2:
        return new_id
    
    else:
        new_id+=new_id[length-1]*(3-length)
        return new_id

def solution(new_id):
    answer = ''
    
    # step 1
    new_id = new_id.lower()
    
    # step 2
    new_id = step_2(new_id)
    
    # step 3,4
    new_id = step_3(new_id)
    
    new_id = step_4(new_id)
    
    # step 5
    if new_id == '':
        new_id += 'a'
        
    # step 6
    if len(new_id)>=16:
        new_id=new_id[:15:]
        
    new_id = step_4(new_id)
    
    # step 7
    answer = step_7(new_id,len(new_id))
    
    
    
    
    
    return answer