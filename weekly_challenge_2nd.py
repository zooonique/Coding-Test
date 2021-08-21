import numpy as np

def check_grade(grade):
    if grade>=90:
        return "A"
    elif grade>=80 and grade<90:
        return "B"
    elif grade>=70 and grade<80:
        return "C"
    elif grade>=50 and grade<70:
        return "D"
    else:
        return "F"


def solution(scores):
    
    answer = ''
    scores = np.transpose(scores)
    
    for i in range(len(scores)):
        self_score = scores[i][i]
        M = max(scores[i])
        m = min(scores[i])
        
        count_M,count_m = 0,0
        
        for c in scores[i]:
            if c==M:
                count_M+=1
            
            elif c==m:
                count_m+=1
                
            else:
                continue
        
        if M == self_score and count_M==1 or count_m==1 and m == self_score:
            grade = (sum(scores[i]) - self_score)/(len(scores)-1)
            
        else:
            grade = (sum(scores[i]))/len(scores)
            
        answer+=check_grade(grade)
        

    
    return answer
