def count_holes(n):
    l = n.lstrip('0')
    m = l.lstrip('-')
    
    for char in l:
        if char.isalpha():
            print("ERROR")
            quit()
        p = '.'
        if p in l:
            print('ERROR')
            quit()
            
    num = ('4', '6', '9', '0')
    b = '8'
    res = 0
    for a in num:
        if a in m:
            res += 1
    if b in l:
        res += 2
    return res

