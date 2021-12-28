class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age =age

    def sit(self):
        """simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")



my_dog = Dog("Joey", 6)

print("\nMy name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()

Jessica_dog = Dog("Ruffus", 10)
print("\nJessica's dog's name is " + Jessica_dog.name.title() + "." )
print("Jessica's dog is " + str(Jessica_dog.age) + "years old.")
Jessica_dog.sit()
Jessica_dog.roll_over()

Robert_dog = Dog("Hercules", 13)
print("\nRobert also has a dog, his name is " + Robert_dog.name.title() + ".")
print("Robert's dog is pretty awesome, however he is getting old. " + Robert_dog.name.title() +
       "is " + str(Robert_dog.age) + " years old.")
Robert_dog.sit()
Robert_dog.roll_over()

David_dog = Dog("Bowzer", 3)
print("\nDavid's dog is rather young. His dog's name is " + David_dog.name.title() + ".")
print(David_dog.name.title() +" is " + str(David_dog.age) + " years old.")
print(David_dog.name.title() + " is pretty well trained, watch this.")
print("Sit !")
David_dog.sit()
print("*The crowd is shocked*")
print(David_dog.name.title() + ", roll over!")
David_dog.roll_over()
