favorite_places = {"Vancouver": "Stacey" , "Japan": "Sam" , "Trinidad":"Sarah", }

print("\nThese are my friend's favorite places in the world: ")
for key, value in favorite_places.items():
    print("\t"+value.title() + "'s " + "favorite place is " + key.title() +".")

