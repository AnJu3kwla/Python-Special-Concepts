from functools import reduce

#Multiply all numbers in a list
data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
multiplier = lambda x, y: x*y

print(reduce(multiplier,data))

product = 1
for i in data:
    product = product * i

print(product)