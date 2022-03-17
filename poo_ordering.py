from functools import total_ordering
from dataclasses import dataclass


@dataclass
@total_ordering
class Personne:
    prenom: str
    age: int

    def __lt__(self, autre):
        return self.age < autre.age

    def __eq__(self, autre):
        return self.age == autre.age


une_personne = Personne(prenom="Georges", age=140)
autre_personne = Personne(prenom="Gertrude", age=80)
troisieme_personne = Personne("Martin", 80)

print(une_personne < autre_personne)
print(une_personne >= autre_personne)

liste_personne = [une_personne, autre_personne]
print(liste_personne)
print(sorted(liste_personne))

print(troisieme_personne == autre_personne)
