def prime_factors(n):
  factors = []
  for i in xrange(2, n+1):
    if n % i == 0:
       if is_prime(i):
         factors.append(i)
  return factors

def is_prime(n):
  for i in xrange(2,n):
    if n % i == 0:
      return False
  return True

def distict_prime_factors(k):
    iter=0
    yes=0
    while (yes != 1):
      jimmy = [0] * k
      for each in range(k):
          jimmy[each] = len(prime_factors(iter+each))
      if jimmy == [k]*k:
          yes = 1
          print "hi"
          return iter
      iter += 1
