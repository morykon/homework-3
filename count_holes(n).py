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
            
    num = ('4', '6', '9', '0')
    b = '8'
    res = 0
    for a in num:
        if a in m:
            res += 1
    if b in m:
        res += 2
    return res

