# from dataclasses import dataclass
#
#
# @dataclass
# class Personne:
#     prenom: str
#     nom: str
#     age: int = 40
#     ville: str = "Brest"
#
#
# une_personne = Personne("Antoine", "Dupont")
# print(une_personne)

class Compte:
    def __init__(self, solde):
        self.solde = solde


class Personne:
    def __init__(self, prenom, nom, solde: int, age=40):
        self.prenom = prenom
        self.nom = nom
        self.age = age
        self.ville = "Brest"
        self.compte = Compte(solde)

    def __repr__(self):
        return f"Nom: {self.nom}, Prenom: {self.prenom}, Solde : {self.compte.solde}"

autre_personne = Personne("Alice", "Dubois", 100)
une_personne = Personne("Alice", "Dubois", 1000)

print(une_personne.ville)
print(une_personne.nom)
print(une_personne)


from random import randint


class FireFighter:
    """
    attrs:
    - position_x: int
    - position_y: int
    methods:
    - move_left() decrease position_x of 1 unit
    - move_right() increase position_x of 1 unit
    - move_up() increase position_y of 1 unit
    - move_down() decrease position_y of 1 unit
    """
    def __init__(self, x_init, y_init):
        self.position_x = x_init
        self.position_y = y_init

    def move_left(self):
        self.position_x -= 1

    def move_right(self):
        self.position_x += 1

    def move_up(self):
        self.position_y += 1

    def move_down(self):
        self.position_y -= 1

    def __repr__(self):
        return f"Firefighter: {self.position_x}, {self.position_y}"


class Board:
    def __init__(self):
        self.firefighter_list = [
            FireFighter(randint(0,10),randint(0,10)) for i in range(4)]

    """
    Faire une methode move_left qui fait tous les pompiers bouger d'une unité sur la gauche
    """
    def move_left(self):
        for firefighter in self.firefighter_list:
            firefighter.move_left()

    def __repr__(self):
        return str(self.firefighter_list)

board = Board()
print(board)
board.move_left()
print(board)

