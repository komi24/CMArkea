# dataclasses
# from functools import total_ordering


class Maison:
    """
    attributs:
    - nb_chambres: int
    - taille du salon: int
    - proprio: None ou str

    methodes:
    - get_surface() sachant que une chambre/cuisine fait la moitié du salon
    - set_proprio()
    """
    def __init__(self, nb_chambres, taille_salon, proprio=None):
        self.taille_salon = taille_salon
        self.nb_chambres = nb_chambres
        self.proprio = proprio

    def get_surface(self):
        return self.taille_salon + (self.taille_salon / 2) * (self.nb_chambres + 1)


ma_maison = Maison(2,4, "toto")
print(ma_maison.get_surface())
