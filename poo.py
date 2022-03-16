from typing import Union


# Faire une classe CompteBancaire
# attributs: solde, proprio, type : "CompteCheque" (default), "CompteEpargne"
class CompteBancaire:
    def __init__(
            self,
            solde:   Union[int, float],
            type_compte="CompteCheque"
    ):
        assert type(solde) in [int, float], "solde doit être une valeur numérique"
        assert type_compte in ["CompteCheque", "CompteEpargne"],\
            "type_compte doit être soit CompteCheque, CompteEpargne"
        self.type = type_compte
        self.solde = solde

    def retrait(self, montant):
        self.solde -= montant

    def depot(self, montant):
        self.solde += montant

un_compte = CompteBancaire(100)
un_compte.retrait(60)
un_compte.depot(80)
print(un_compte.solde)

class Personne:
    def __init__(self, firstname, lastname, solde=1000, age=73):
        self.prenom = firstname
        self.nom = lastname
        self.age = age
        self.compte = CompteBancaire(solde)

    def se_presenter(self):
        print(f"Bonjour je m'appelle {self.prenom}. J'ai {self.age} ans")

    def se_presenter_a(self, autre: "Personne"):
        print(f"Bonjour {autre.nom}, je m'appelle {self.nom}")

    def transfert_a(self, autre, montant):
        self.compte.retrait(montant)
        autre.compte.depot(montant)


personne = Personne("Olivier", "Dubois")
autre_personne = Personne("Abdel", "Martin")
personne.se_presenter()
personne.se_presenter_a(autre_personne)
personne.transfert_a(autre_personne, 100)
print(personne.compte.solde)