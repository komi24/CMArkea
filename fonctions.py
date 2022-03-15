# def dire_bonjour():
#     print("Bonjour")
#
# dire_bonjour()
# dire_bonjour()

def dire_bonjour(name):
    """
    Dit bonjour à [name]
    :param name: Nom de la personne à saluer (obligatoire)
    :return:
    """
    print(f"Bonjour {name}")

# help(dire_bonjour)
dire_bonjour("Alice")

def dire_bonjour(name="Bob"):
    print(f"Bonjour {name}")

dire_bonjour("Alice")


def dire_bonjour(age: int, name: str="Bob") -> str:
    return f"Bonjour {name}. Tu as {age} ans ?"


dire_bonjour(52)
dire_bonjour(name="Alice", age=36)

nom = "Alice"
def dire_bonjour(age: int, name: str="Bob") -> str:
    name = "Bernard"
    return f"Bonjour {name}. Tu as {age} ans ?"

print(dire_bonjour(28, nom))
print(nom)


noms = ["Alice"]
def dire_bonjour(age: int, names: list=["Bob"]) -> str:
    names[0] = "Bernard"
    return f"Bonjour {names[0]}. Tu as {age} ans ?"

print(dire_bonjour(28, noms))
print(noms)

noms = ["Alice"]
def dire_bonjour(age: int, names: list=["Bob"]) -> str:
    names = ["Bernard"]
    return f"Bonjour {names[0]}. Tu as {age} ans ?"

print(dire_bonjour(28, noms))
print(noms)



name = "Alice"

def dire_bonjour(nom):
    global name
    name = "Martin"
    print(name)

print(name)
dire_bonjour(name)
print(name)



name = "Alice"

def dire_bonjour(nom):
    nom = "Martin"
    print(nom)

print(name)
dire_bonjour(name)
print(name)



name = {"nom": "Alice"}

def dire_bonjour(nom):
    nom["nom"] = "Martin"
    print(nom)

print(name)
dire_bonjour(name)
print(name)


def add(a, b):
    return a + b

print(add(2, 4 ))
print(add("Bonjour ", "Martin"))

ma_liste = [2,8,6,7]
print(list(map(lambda x:x*2, ma_liste)))
print([x*2 for x in ma_liste])


liste_ages = [15, 32, 56, 48, 23]
liste_prenoms = ["Alice", "Bob", "Christophe", "Geroges", "Helene"]

personnes = [
    {"prenom": prenom, "age": age} for age, prenom in zip(liste_ages, liste_prenoms)]
print(list(map(lambda x:x["age"], personnes)))
print([x["age"] for x in personnes])

