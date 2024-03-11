x, y = 0, 1
 
def gcdExtended(a, b):
    global x, y
    if (a == 0):
        x = 0
        y = 1
        return b
    gcd = gcdExtended(b % a, a)
    x1 = x
    y1 = y
    x = y1 - (b // a) * x1
    y = x1
 
    return gcd
 
 
def modInverse(A, M):
 
    g = gcdExtended(A, M)
    if (g != 1):
        print("Inverse doesn't exist")
 
    else:
 
        # m is added to handle negative x
        res = (x % M + M) % M
        print("Modular multiplicative inverse is ", res)

def solveK (k1, gcd, p, r):
    k = k1
    for i in range(1, gcd + 1):
        if 2**k % p == r:
            return k
        k += (p+1)/gcd
    return k
if __name__ == "__main__":
    A = 50910
    M = 112559
    solveK(1814, 6, 65539, 18357)

    modInverse(A, M)