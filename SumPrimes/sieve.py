# returns list of prime truths - size = limit
def primes(limit):
  a = [True] * limit # Initialize the primality list
  a[0] = a[1] = False

  for (i, isprime) in enumerate(a):
    if isprime:
      for n in xrange(i*i, limit, i): # Mark factors non-prime
        a[n] = False
  return a
