def solution(board, moves):
    answer = 0
    stack = []
    
    for m in moves:
        for b in board:
            if b[m-1] == 0:
                continue
            
            else:
                stack.append(b[m-1])
                b[m-1]=0
                break
        
                
        if len(stack)>1 and stack[len(stack)-1]==stack[len(stack)-2]:
            answer += 2
            stack.pop()
            stack.pop()
        
    
    
    return answer