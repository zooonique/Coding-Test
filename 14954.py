n = input()
data = []


while True:
    res=0
    for i in n:
        res+=int(i)**2
    
    if res==1:
        print("HAPPY")
        break
    
    elif res in data:
        print("UNHAPPY")
        break
    
    else:
        data.append(res)
        n=str(res)