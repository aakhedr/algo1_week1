def regularMul(x, y):
    '''Python regular multiplication'''
    return x * y

def karatsuba(x, y):
    ''' recusive implementation of karatsuba multiplication algorithm '''
    if len(str(x)) == 1 and len(str(y)) == 1:
        return x * y

    n = 0
    if len(str(x)) == len(str(y)) and len(str(x)) % 2 == 0:
        n = len(str(x))
    a = int(str(x)[:n/2])
    print 'a', a
    b = int(str(x)[n/2:])
    print 'b', b
    c = int(str(y)[:n/2])
    print 'c', c
    d = int(str(y)[n/2:])
    print 'd', d

    p1 = karatsuba(a, c)
    p2 = karatsuba(b, d)
    p3 = karatsuba((a+b), (c+d))
    return p3 - p2 - p1
