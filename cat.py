class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def fetch(self):
        print(self.name.title() + " is fetching the toy.")

    def attack(self):
        print(self.name.title() + " is in attack mode.")

my_cat = Cat("Corkie", 3)

print("My cat's name is " + my_cat.name.title() + ".")
print("He is " + str(my_cat.age) + " years old.")
print("I've taught him several things over the years, watch this.")
print(my_cat.name.title() + " FETCH! ")
my_cat.fetch()
print("\n*the crowd claps.")
print("\nI've even taught him to defend the house.")
print(my_cat.name.title() + ", defend the house!")
my_cat.attack()
print("*The crowd goes APE SHIT!")


