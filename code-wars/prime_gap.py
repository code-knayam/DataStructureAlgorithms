# The prime numbers are not regularly spaced. For example from 2 to 3 the gap is 1. From 3 to 5 the gap is 2. From 7 to 11 it is 4. Between 2 and 50 we have the following pairs of 2-gaps primes: 3-5, 5-7, 11-13, 17-19, 29-31, 41-43

# A prime gap of length n is a run of n-1 consecutive composite numbers between two successive primes (see: http://mathworld.wolfram.com/PrimeGaps.html).

# We will write a function gap with parameters:

# g (integer >= 2) which indicates the gap we are looking for

# m (integer > 2) which gives the start of the search (m inclusive)

# n (integer >= m) which gives the end of the search (n inclusive)

def gap(g, m, n):
    # your code
    primeList = []
    for i in range(m,n+1):
        if isPrime(i):
            primeList.append(i)

    for i in range(len(primeList)-1):
        if primeList[i] + g == primeList[i+1]:
            return [primeList[i], primeList[i+1]]

    return None


# def gap(g, m, n):
#     # your code
#     while m <= n:       
#         if isPrime(m) and isPrime(m+g):
#             index = m + 1
#             consec = True
#             while index < (m+g-1) and consec:
#                 if isPrime(index):                    
#                     consec = False
#                 index = index + 1
#             if consec:
#               return [m, m+g]
#         m = m + 1
#     return None
    
def isPrime(num):
    return all(num % i for i in range(2, num))


print(gap(2,100,110))
print(gap(4,100,110))
print(gap(6,100,110))
print(gap(8,300,400))
print(gap(10,300,400))