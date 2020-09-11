def f(x):
    return 3*x + 1

print(f(2))

"""Lambda Expression"""
lambda x : 3*x + 1
#We can't use this function anywhere because it has no name. So we can give it a name and then get use of it
g = lambda x: 3*x + 1
print(g(2)) 

"""Lambda Expressions with multiple inputs"""
full_name = lambda first_name, last_name : first_name.strip().title() + " " + last_name.strip().title()
print(full_name("pULithA", "AnjANa"))

scifi_authors = ["Issac Asimov", "Ray Bradbury", "Robert Heinlein", "Arthurs C. Clarke", "Frank Herbert", "Orson Scott Card", "Duglas Adams", "H.G.Wells","Leigh Brackett"]

scifi_authors.sort(key = lambda name : name.split(" ")[-1].lower())
print(scifi_authors)

def build_quadratic_function(a,b,c):
    """Returns the function f(x) = ax^2 + bx + x"""
    return lambda x:a*x**2 + b*x + c

f = build_quadratic_function(2,3,-5)
print(f(0))
print(f(1))
print(f(2))

print(build_quadratic_function(3,0,1)(2))