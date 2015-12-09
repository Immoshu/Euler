def isPalindrome(number):
  # [::-1] reverse string
  return str(number) == str(number)[::-1]

def loopRange(low, high):
  maximum = 0
  for x in range(low, high):
    for y in range(low, high):
      product = x*y
      if(isPalindrome(product)):
        if(product > maximum):
          maximum = product
  return maximum

print loopRange(100, 999)  
