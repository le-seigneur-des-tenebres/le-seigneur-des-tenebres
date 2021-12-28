friend_1 = {"first name": "John", "last name": "kim", "age": 29, "city": "Toronto", }
friend_2 = {"first name": "Austen", "last name": "Scruggs", "age": 26, "city": "Athens", }
friend_3 = {"first name": "harry", "last name": "potter", "age": 28, "city": "Godric's Hollow", }

people = [friend_1, friend_2, friend_3]

for friend in people:
    print("\n")
    for key, value in friend.items():
        print(key.title() + ": ")
        print(str(value).title())