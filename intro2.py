print(3 | 2)  # 11 | 10
print(3 & 2)  # 11 & 10

ma_liste = [0] * 100
print(ma_liste)
print(len(ma_liste))

ma_chaine = "Bonjour Mickael"
# ma_chaine[0] = "C" # Erreur
ma_chaine = "Bonjour Martine"
print(ma_chaine)


dico_1 = {"prenom": "Martin", "nom": "Leroy"}
dico_1["prenom"] = "Eliane"
print(dico_1)

dico_2 = dico_1
dico_2["prenom"] = "Georges"
print(dico_2)
print(dico_1)
dico_2 = {"prenom": "Martin", "nom": "Kern"}
print(dico_1)

dico_2 = dico_1.copy()
dico_2["prenom"] = "Alice"
print(dico_1)
print(dico_2)

print("Deep copy ?")
dico_1 = {"prenom": "Martin", "nom": "Leroy", "adresse": {"ville": "Brest", "pays": "France"}}
dico_2 = dico_1.copy()
dico_2["prenom"] = "Alice"
dico_2["adresse"]["pays"] = "Bretagne"

print(dico_1)
print(dico_2)

print("Deep copy ?")
from copy import deepcopy

dico_1 = {"prenom": "Martin", "nom": "Leroy", "adresse": {"ville": "Brest", "pays": "France"}}
dico_2 = deepcopy(dico_1)
dico_2["prenom"] = "Alice"
dico_2["adresse"]["pays"] = "Bretagne"

print(dico_1)
print(dico_2)


liste_ages = [15, 32, 56, 48, 23]
liste_prenoms = ["Alice", "Bob", "Christophe", "Geroges", "Helene"]

personnes = [
    {"prenom": prenom, "age": age} for age, prenom in zip(liste_ages, liste_prenoms)]
print(personnes)


# Structures conditionnelles
age = 17
pays = "France"
if age > 18:
    print("Majeur")
elif age == 18 and pays == "France":
    print("passe ton permis")
elif age == 18:
    print("pass the licence exam")
else:
    print("Mineur")



etat = "mineur" if age < 18 else "majeur"
print(etat)


# Boucles
ma_liste = [5, 48, 62]
for element in ma_liste:
    print(element)

for i in range(len(ma_liste)):
    print(ma_liste[i])

for i, val in enumerate(ma_liste):
    print(f"L'indice est {i}, la valeur est {val}")

print(range(12))
print(list(range(12)))

personnes = [
    {"prenom": prenom, "age": age} for age, prenom in zip(liste_ages, liste_prenoms)]
print(personnes)

from itertools import product

ages = [18, 25, 35]
prenoms = ["Martin", "Helene"]
for age, prenom in product(ages, prenoms):
    print(f"Je suis {prenom} et j'ai {age} ans")

# Tri bulle
ma_liste = [3, 1, 15, 8, 12, 0]

for i in range(len(ma_liste)):
    if ma_liste[i] > ma_liste[i+1]:
        # echanger
        print("échanger")

print(ma_liste)