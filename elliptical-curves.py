
def inverse(a,p):
    if p == 1:
        return 1/a
    return pow(a, p-2, p)

def find_m(P,Q,p,b):
    m = 0;
    x1, y1 = P
    x2, y2 = Q
    if(x1 == x2 and y1 == y2):
        x = (3 * x1**2) + b
        print('before')
        print(x)
        x = x % p
        print('after')
        print(x)
        y = 2 * y1
        if y == 0:
            return 'inf'
        y = inverse(y,p)
        m = x*y
        m = m % p
    else:
        y = y2 - y1
        y = y % p
        x = x2 - x1
        x = x % p
        if x == 0:
            return 'inf'
        x = inverse(x, p)
        m = x * y
        m = m % p
    return m 

def addition(P, Q,p,b):
    if P == 'inf':
        return Q
    if Q == 'inf':
        return P
    m = find_m(P,Q,p,b)
    x1, y1 = P
    x2, y2 = Q
    if m == 'inf':
        return 'inf'
    x3 = (m**2) - x1 - x2
    x3 = x3 % p
    y3 = m * (x1 - x3) - y1
    y3 = y3 % p
    return (x3, y3)

def order(P, p, b):
    #x ,y = P
    Q = P
    count = 1
    res = 0
    while(1):
        res = addition(Q,P,p,b)
        if res == 'inf':
            break;
        Q = res
        count+=1
    return count

def find_m(P,Q,b):
    m = 0;
    x1, y1 = P
    x2, y2 = Q
    if(x1 == x2 and y1 == y2):
        x = (3 * x1**2) + b
        y = 2 * y1
        if y == 0:
            return 'inf'
        y = inverse(y,p)
        m = x*y
    else:
        y = y2 - y1
        x = x2 - x1
        if x == 0:
            return 'inf'
        x = inverse(x, p)
        m = x * y
    return m

def addition (P, Q, b):
    if P == 'inf':
        return Q
    if Q == 'inf':
        return P
    m = find_m(P,Q,b)
    x1, y1 = P
    x2, y2 = Q
    if m == 'inf':
        return 'inf'
    x3 = (m**2) - x1 - x2
    y3 = m * (x1 - x3) - y1
    return (x3, y3)

def order(P, b):
    #x ,y = P
    Q = P
    count = 1
    res = 0
    while(1):
        res = addition(Q,P,b)
        if res == 'inf':
            break;
        Q = res
        count+=1
    return count

def kP(P, k, b):
    Q = None
    while k > 0:
        if k % 2 == 1:
            if Q is None:
                Q = P
            else:
                Q = addition(Q, P, b)
        P = addition(P, P, b)
        k //= 2
    return Q


P = (3,5)
#Q = (1,0)
#p = 1
b = 0

#print(kP(P, 7, b))

print((115*5 + 323*12) % (19*23))
print((19*23))



#remainder(13)