found = False
value = 2520
increment = 10
top = 20
base = 1

#get maximum increment before starting
for x in range (20, 10, -1):
  if value % x == 0:
    increment = x
    break

#loop till conditions (1-20 evenly divdes) are met
while(not found):
  #assume true at start of loop and check for falseness
  found = True

  #loop backwards want to break on higher numbers first then jump max increment
  #no need divide by one - need see if case to avoid % 2
  for x in range(20, 1, -1):
    if (value % x) != 0:
      value += increment
      found = False
      break

  if found:
    print value
	
  
