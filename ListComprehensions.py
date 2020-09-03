squares = []
for i in range(1, 101):
    squares.append(i**2)

print(squares)

sqaures2 = [i**2 for i in range(1, 101)]
print(sqaures2)

remainders5 = [x**2 % 5 for x in range(1, 101)]
print(remainders5)

remainders11 = [x**2 % 11 for x in range(1,101)]
print(remainders11)

movies = ["Star Wars", "Ghandhi", "Casablanca", "Shawshank Redemption", "Toy Story", "Gone with the wind", "Citizen Cane", "It's awonderful life", "The wizard of Oz", "Gattaca", "Rear Window", "Ghostbusters", "To kill A Mockingbird", "Good will Hunting", "2001: A space Odyssey", "Raiders of the Lost Ark", "Grounding Day", "Close Encounters of the Third Kind"]
gmovies = []
for title in movies:
    if title.startswith("G"):
        gmovies.append(title)

gmovies = [title for title in movies if title.startswith("G")]
print(gmovies)

movie_details = [("Citizen Kane", 1941), ("Spirited Away", 2001), ("It's a Wonderful Life", 1946), ("Gattaca", 1997), ("No Country for Old Men", 2007), 
("Rear Window", 1954), ("The Loard of the Rings: The Fellowship of the Ring", 2001), ("Groundhog Day", 1993), ("Close Encounters of the Third Kind", 1977),
("The Royal Tenebaums", 2001), ("The Aviator", 2004), ("CRaiders of the Lost Ark", 1981)]

pre2k = [title for (title, year) in movie_details if year < 2000]
print(pre2k)

v = [2, -3, 1]
4*v
print(4*v) #In here, the same lis is concatenated 

vm = [4*i for i in v]
print(vm)

"""List Comprehension for Cartisian Product"""

A = [1, 3, 5, 7] #elements of A taken as a
B = [2, 4, 6, 8] #elements of B taken as b

cartisian_product = [(a,b) for a in A for b in B]
print(cartisian_product)