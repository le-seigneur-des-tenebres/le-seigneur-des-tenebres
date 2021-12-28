Hercules = {"pet's name": "Hercules", "type of animal" : "cat", "owner's name": "Byron"}
Lucky = {"pet's name": "Lucky", "type of animal" : "cat", "owner's name": "Stephanie"}
Corkie = {"pet's name": "Corkie", "type of animal" : "cat", "owner's name": "Promyce"}
Buddy = {"pet's name": "Buddy", "type of animal" : "cat", "owner's name": "Shane"}
Santa = {"pet's name": "Santa", "type of animal" : "dog", "owner's name": "Tanya"}

pets = [Hercules, Lucky, Corkie, Buddy, Santa]

print("\n")
print("These are our pets: ")
for pet in pets:
    for key, value in pet.items():
        print(key.title() + ": " + value.title())
    print("\n")
