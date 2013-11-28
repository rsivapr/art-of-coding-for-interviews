def self_powers(n):
  sum = 0
  for i in xrange(n):
    sum += (i ** i) % (10**10)
  return sum % (10 ** 10)

if __name__ == '__main__':
    self_powers(1000)
