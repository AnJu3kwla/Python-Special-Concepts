import math

def area(r):
    """Area of a circle with radius 'r'."""
    return math.pi * (r**2)

radii = [2, 5, 7.1, 0.3, 10]
print(radii)

#Method 1: Direct method

areas = []
for r in radii:
    a = area(r)
    areas.append(a)

print(areas)   

#Method 2: Use 'map'  function 

"""map() function has to arguments [1].function , [2]. list / tuple or other itarable object"""
m = map(area,radii)  
print(m) #Out put is not a list but a map object
print(list(map(area,radii)))

temps = [("Berlin",29), ("Cairo",36), ("Buenos Aires",19), ("Los Angeles",26), ("Tokyo",27), ("New York",28), ("London",32), ("Beijing",32)]

c_to_f = lambda data : (data[0], (9/5)*data[1] + 32)
print(list(map(c_to_f,temps)))