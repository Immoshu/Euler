num = 100

# standard maths definitions for sum(n) and sum(n^2)
sumNumSquared = ((num * (num + 1))/2) ** 2
sumSquares = (num * (num + 1) * ((2 * num) + 1))/6
print sumNumSquared - sumSquares
