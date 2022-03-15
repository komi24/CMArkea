# Ceci est un commentaire
print("Bonjour")  # Affiche Bonjour

"""
Ceci est une docstring 
sur plusieurs lignes
"""

a = 10

print(a + 2)
print(type(a))

a = "Bonjour"
print(type(a))

a = 10
b = 12
print(a + b)

a = "10"
b = "12"
print(a + b)
print(int(a) + int(b))

# print(int(a) + b)


a = [1,2,3]
b = 4
print(a * b)

a = 4j
print(a**2)

a = False
b = True

variable_1 = "Bonjour"
# 1variable = "Salut"

ma_liste = [4, 8 , 9, 21, 51, 98, 78]
mon_autre_liste = [4, 2, True, ["Bonjour", None], 12]

print(ma_liste)
print(mon_autre_liste[0])
print(mon_autre_liste[1])
print(mon_autre_liste[-1])
print(mon_autre_liste[-2])
print(mon_autre_liste[-2][0])

print(len(ma_liste))

print(ma_liste[0:2])
print(ma_liste[:2])
print(ma_liste[1:])
print(ma_liste[:-1])

ma_liste = [4, 8 , 9, 21, 51, 98, 78]
print(ma_liste[0:4:2])

print(ma_liste[::-2])

ma_liste = [4, 8 , 9, 21, 51, 98, 78]
print("afficher le premier élément")
print(ma_liste[0])
# afficher le premier élément
print("afficher le dernier élément")
print(ma_liste[-1])
# afficher le dernier élément
print("afficher les 4 premiers éléments")
print(ma_liste[:4])
# afficher les 4 premiers éléments
print("afficher les deux derniers éléments")
print(ma_liste[-2:])
# afficher les deux derniers éléments
print("afficher les éléments du 2ème au 5ème (inclus)")
print(ma_liste[1:5])
# afficher les éléments du 2ème au 5ème (inclus)
print("afficher les éléments du 6ème (inclus) au 3ème (inclus) en sens inverse")
print(ma_liste[5:2:-1])
# afficher les éléments du 6ème (inclus) au 3ème (inclus) en sens inverse

prenom = "Mickael"
age = 30
print(f"Bonjour {prenom}, j'ai {age} ans. Je dit : \"Salut\"")
print("Bonjour %s"%(prenom))
print("Bonjour %s, j'ai %d ans"%(prenom, age))

mon_dico = {"nom": "Bolnet", "age": 35, 32: True, True: "C'est l'heure de la pause"}

age = 38
condition = age > 18
print(mon_dico[condition])

mon_tuple = (3, 2)
print(mon_tuple[0])

print(ma_liste)
ma_liste[0] = 475
print(ma_liste)

mon_tuple[0] = 16







