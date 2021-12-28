mountains = ["killamnjaru", "Everest", "Stone Mountain", "Rushmore", "Rocky Mountains"]

rivers = ["Danabue", "Mississippi", "Occonee", "DonValley River", "Nile", "Sticks"]

countries = ["Le Canada", "Les Etats-Unis", "La France", "L'Angleterre", "Le Nigere"]

languages = ["l'anglais", "le francais", "l'italien", "le japonais", "l'espagnol", "le chinois"]

mountains.sort()
print(mountains)
rivers.sort(reverse=True)
print(rivers)

rivers.reverse()
print(rivers)

print(len(countries))

print(sorted(languages))