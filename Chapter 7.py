nombre = input("Entrez un nombre, et je vous dirais si c'est un nombre pair ou un nombre impair: ")
nombre = int(nombre)

if nombre % 2 == 0:
    print("\nLe nombre " + str(nombre) + ", il est un nombre pair.")
else:
    print("\nLe nombre " + str(nombre) + ", il est un nombre impair.")