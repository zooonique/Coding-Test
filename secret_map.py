def change(text):
    text = text.replace('1','#')
    text = text.replace('0',' ')
    return text

def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        OR = bin(arr1[i]|arr2[i])[2::]
        
        if n > len(OR):
            OR = '0'*(n-len(OR))+OR
        
        answer.append(change(OR))
    
    return answer
