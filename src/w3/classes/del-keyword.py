class BB:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is ", self.name)
        print("Hello my age is ", self.age)

p1 = BB("AA", 12)
p1.myfunc()
del p1.name
p2= BB("bb", 23)
p2.myfunc()
del p2
print ( p1.age)
