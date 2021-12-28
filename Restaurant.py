"""
9-1. Restaurant: Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indicating
that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes
individually, and then call both methods.

"""
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restuarant(self):
        print(restaurant_name.title() + " is an amazing place to eat, the food is amazing. They specialize in " + cuisine_type.name.title() +"." )

    def open_restauran(self):
        print(restaurant_name.name.title() + " is open." + " Would you like to book a reservation ?")


good_eats = Restaurant("Sauce House", "Southern BBQ")

print(good_eats.restauraant_name.title())
print(good_eats.cuisine_type.title())
print("I love that place.")





