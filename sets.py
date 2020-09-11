#Order doesn't matter in Sets. But in lists and tuples order matters

example = set()
print(dir(example))

#help(example.add)

example.add(26)
example.add(False)
example.add(3.14159)
example.add("Thorium")

print(example)
print(len(example))

#Removing element
example.remove(26)
print(len(example))

"""In remove method, if we try to remove an element which is not in the set gives an error"""
# example.remove(50)
# print(len(example))

"""But in discard method if we try to remove an element which is not in the set won't gives an error"""
example.discard(50)
print(len(example))

example2 = set([42,True,2.71828,"Helium"])
len(example2)

example2.clear()
len(example2)

#Integers 1-10
odds = set([1,3,5,7,9])
evens = set([2,4,6,8,10])
primes = set([2,3,5,7])
composites = set([4,6,8,9,10])

print(odds.union(evens))
print(evens.union(odds))
print(odds)
print(evens)
print(odds.intersection(primes))
print(primes.intersection(evens))
print(odds.intersection(evens))

print(2 in primes)
print(6 not in odds)