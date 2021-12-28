favorite_numbers = {"sarah": [6, 12, 18, 39], "sam": [3, 7, 11, 57, 61], "stephanie": [51], "stephen": [93, 30, 56, 89, 33], "Stan": [7], "Samantha": [666], }
print("These are my friends favorite numbers.")
for key, value in favorite_numbers.items():
    if len(value) >= 2:
        print(key.title() + "'s favorite numbers are: ")
        print("\t" + str(value).strip("[]"))
        print("\n")
    else:
        print(key.title() + "'s favorite number is: ")
        print("\t" + str(value).strip("[]"))
        print("\n")