
squares = []

for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

the_box = []
for value in range(1,11):
    the_box.append(value**2)
print(the_box)

comprehension = [value**2 for value in range(1,11)]
print(comprehension)