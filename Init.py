import datetime

class User:
    #Adding Docstring

    """A member of FriendFace. For now we are only storing their name birthday. But soon we will
    store an uncomfortable amount of user information"""

    def __init__(self, full_name, birthday):
        #self --> reference to the new object created 
        self.name = full_name
        self.birthday = birthday #yyyymmdd

    #Extract first and last names
        name_pieces = full_name.split(" ") #chop the full name in to pieces when it encounters a space and then stores that pieces in an array called name_pieces
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

    def age(self):
        """Return te age of the user in years"""
        today = datetime.date(2001, 5, 12)
        #Converting birthday string to a date object
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        #By using above integers we can make the date object for the birthay
        dob = datetime.date(yyyy, mm, dd) #Date of Birth 
        age_in_days = (today - dob).days #we get a time delta object. time delta object has a field called days
        age_in_years = age_in_days / 365
        return int(age_in_years)

help(User)

user = User("Pulitha Anjana", "19941101")
print(user.name)
print(user.first_name)
print(user.last_name)
print(user.birthday) 
print(user.age())
#print(user)  