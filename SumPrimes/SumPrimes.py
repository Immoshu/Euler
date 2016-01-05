import sieve
primeList = sieve.primes(2000000)
tot = 0
for index, truth in enumerate(primeList):
  if truth:
    tot += index

print tot
