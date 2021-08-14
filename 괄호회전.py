def solution(s):
    answer = 0
    sample = ['()','{}','[]']
    case = s
    for cnt in range(len(s)):
        # n번 rotate
        case = case[1:len(s):]+case[0]
        tmp = case
        while case:
            if sample[0] in case:
                case=case.replace(sample[0],'')
            
            elif sample[1] in case:
                case=case.replace(sample[1],'')
                
            elif sample[2] in case:
                case=case.replace(sample[2],'')
                
            else:
                answer-=1
                break
                
        answer += 1
        case = tmp
            
    
    return answer
