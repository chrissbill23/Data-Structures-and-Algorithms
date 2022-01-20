def binomialCoef(n,k):
    if n < 2*k:
        k = n-k
    res = 1
    for i in range(k):
        res*=(n-i)
        res//=(i+1)
    return res
  
def catalanNumbers(n: int) -> int:
    res = 1
    for i in range(1, n+1):
        res *= (4 * i - 2);
        res //= (i + 1);
    return res
  
