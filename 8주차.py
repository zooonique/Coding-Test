def solution(sizes):
    
    arr1,arr2 = [],[]
    for i in sizes:
        arr1.append(max(i))
        arr2.append(min(i))
            

    
    return max(arr1)*max(arr2)
