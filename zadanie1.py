import math

def isPrime(n:int)->bool:
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

def primes():
    tab = []
    for i in range(3,101):
        if isPrime(i):
            tab.append(i)
    return tab

def goldbach(n: int):
    rmax = -1
    a = 0
    b = 0
    tprimes = primes()
    for i in tprimes:
        for j in tprimes:
            r = math.fabs(j-i)
            if n==i+j and i<=j and r>rmax:
                a = i
                b = j
                if r>rmax: rmax = r
    return a,b
