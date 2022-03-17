from typing import Union
from dataclasses import dataclass


# Faire une classe CompteBancaire
# attributs: solde, proprio, type : "CompteCheque" (default), "CompteEpargne"
@dataclass
class CompteBancaire:
    solde: int
    # def __init__(
    #         self,
    #         solde:   Union[int, float],
    # ):
    #     assert type(solde) in [int, float], "solde doit être une valeur numérique"
    #     self.solde = solde

    def retrait(self, montant):
        self.solde -= montant

    def depot(self, montant):
        self.solde += montant

    # def __repr__(self):
    #     return f"Compte : {self.solde}"


class CompteEpargne(CompteBancaire):
    def retrait(self, montant):
        if self.solde > montant:
            # CompteBancaire.retrait(self, montant)
            super().retrait(montant)
        else:
            raise Exception


class CompteCheque(CompteBancaire):
    def __init__(self, solde, decouvert_max):
        super().__init__(solde)
        # CompteBancaire.__init__(self, solde)
        self.decouvert_max = decouvert_max

    def retrait(self, montant):
        if self.solde + self.decouvert_max > montant:
            # CompteBancaire.retrait(self, montant)
            super().retrait(montant)
        else:
            raise Exception



un_compte = CompteBancaire(100)
compte_epargne = CompteEpargne(10000)
compte_cheque = CompteCheque(100, 100)
un_compte.retrait(60)
un_compte.depot(80)
print(un_compte.solde)
print(compte_epargne)
compte_cheque.retrait(20)
print(compte_cheque)

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