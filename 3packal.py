def pack(n):   
    j = 0
    l = [1]
    
    while j < n:
    
        r = []
        for i in range(0,len(l)-1):
            k = l[i] + l[i+1]
            r.append(k)
            #print(r)
        l = [1] + r + [1]
        j += 1
    return l

print(pack(int(input())))
