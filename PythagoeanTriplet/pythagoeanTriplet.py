n = 1000
found = False
for a in range (1, n/3):
  for b in range(a+1, n/2):
    c = n - b - a
    #We're told there is exaxtly one triplet => only need check pythagoeran conidtion
    if((a * a) + (b * b) == (c * c)):
      found = True
      print a * b * c
      break
  if found:
    break

    
