def count_holes(n):
    l = n.lstrip('0')
    m = l.lstrip('-')
    
    for c in m:
        if c.isalpha():
            print("ERROR")
            quit()
        p = '.'
        if p in m:
            print('ERROR')
            quit()
            
    b = '8'
    u = '4'
    h = '6'
    r = '9'
    q = '0'
    res = 0
    for t in m:
        if u in t:
            res += 1
        if h in t:
            res += 1         
        if b in t:
            res += 2
        if q in t:
            res += 1 
        if r in t:
            res += 1             
        
    return res
