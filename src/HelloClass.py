# The self parameter is a reference to the current instance of the class,
# and is used to access variables that belongs to the class.
# It does not have to be named self , you can call it whatever you like,
# but it has to be the first parameter of any function in the class:

class Hello11:
    welcome = "Hello World!!!"

class Hello22:
# The __init__() function is called automatically every time
# the class is being used to create a new object.
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Hello33:
    def __init__(helloself, guest, id):
        helloself.guest = guest
        helloself.id = id

    def welcomeGuest(self):
        print("Guest Id is: ", self.id)

h1 = Hello11()
print(h1.welcome)

h2 = Hello22("JK", 22)
print("Name is: ", h2.name)
print("Id is: ", h2.id)

h3 = Hello33("Guest 33 !!!", 33)
print("Name is: ", h3.guest)
print("Id is: ", h3.id)

h3.welcomeGuest()


