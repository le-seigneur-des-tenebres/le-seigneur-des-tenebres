favorite_numbers = {"Samantha": [45, 43, 5, 5, 7, 92], "Sam": [4, 65, 35, 75, 92], "Sophie": [43, 34, 53, 36, 83, 98],
                    "Stan": [9, 21, 32, 93, 200], "Sean":[8], "Stephanos": [43, 3]}
print("\n")
print("These are my friend's favorite numbers")
for key, value in favorite_numbers.items():
    if len(value) >= 2:
        print(key.title() + "'s favorite numbers are: ")
        print("\t" + str(value).strip("[]"))
    else:
        print(key.title() + "'s favorite number is:")
        print(str(value).strip("[]"))