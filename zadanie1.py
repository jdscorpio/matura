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


