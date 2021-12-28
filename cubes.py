cubes = []
for value in range(1,11):
    cubes.append(value**3)
print(cubes)

print("\nThese are the first ten cubes from 1 to 10")

#This should produce an identical list, except this time I'm going to aim for a comprehension

CUBES = [ VALUE**3 for VALUE in range(1,11)]
print((CUBES))

#This should produce an identical list as well, but this time I'm going to aim for a less concise line of code

Cubes = []
for Value in range(1,11):
    Cube = Value**3
    Cubes.append(Cube)
print(Cubes)