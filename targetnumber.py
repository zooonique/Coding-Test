'''
# 완전 탐색

from itertools import product

def solution(numbers, target):
    answer = 0
    
    p = []
    
    for i in numbers:
        p.append((i,-i))
    
    sum_list = list(map(sum, product(*p)))
    
    answer = sum_list.count(target)
    
    return answer
    
'''


def dfs(idx, res, numbers, target):
    global answer
    if idx == len(numbers):
        if res == target:
            answer+=1
        
        return
    
    dfs(idx+1,res+numbers[idx],numbers,target)
    dfs(idx+1,res-numbers[idx],numbers,target)
    
    
def solution(numbers, target):
    global answer
    answer = 0
    
    
    dfs(0,0,numbers,target)
    
    return answer