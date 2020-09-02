class User:
    pass

user1 = User()
user1.first_name = "Pultha"
user1.last_name = "Anjana"

print(user1.first_name)
print(user1.last_name)

#classes can have different values for the same variable name
user2 = User()
user2.first_name = "John"
user2.last_name = "Doe"

print(user2.first_name)
print(user2.last_name)
print(user2.first_name,user2.last_name)

user1.age = 26
user2.favourite_book = "2001 : A Space Odyssey"