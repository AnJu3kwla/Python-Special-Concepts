#Alkaline Eart metals

earth_metals = ["Beryllium", "Magnesium", "Calcium", "Strontium", "Barium", "Radium"]
earth_metals.sort()
print(earth_metals) #For acending order

earth_metals.sort(reverse = True)#For decending order
print(earth_metals)

#sort() function can't be use in tuples. We use sorted() function for tuples
"""Tuples are immutable objects they can't change. According to the 'in-place' Algorithm, python does not create 
   a 2nd data structure and modify the existing structure"""

"""format = (name, radius, density, distance from sun)

   Radius : Radius at eqator in kilometers
   Density: Average density in g/cm3
   Distance from sun : Avg. distance of earth to Sun in Aus
   
   1 Astronomical Unit = Average distance of Earth to sun (approximatly equals)"""

planets = [("Mercury",2440, 5.43, 0.395),
           ("Venus", 6052, 5.24, 0.723),
           ("Earth",6378, 5.52, 1.000),
           ("Mars",3396, 3.93, 1.530),
           ("Jupiter",71492, 1.33, 5.210),
           ("Saturn",60268, 0.69, 9.551),
           ("Uranus",25559, 1.27, 19.213),
           ("Neptune",24764, 1.64, 30.070)]

size = lambda planet: planet[1]
planets.sort(key = size, reverse = True)

density = lambda planet: planet[2]
planets.sort(key = density, reverse = True)
print(planets)

#Sorting tuples
sort_earth_metals = sorted(earth_metals)
print(sort_earth_metals)

data = (4,8,9,2,7,1,3,6,5,10)
print(sorted(data))
print(data)

print(sorted("Python"))