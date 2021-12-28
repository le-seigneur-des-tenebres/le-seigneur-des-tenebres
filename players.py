players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

print("\nHere are the first 3 players names: ")
for name in players[:3]:
    print(name.title())

