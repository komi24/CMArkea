
def dire_bonjour(nom):
    assert type(nom) == str, "Nom doit être une chaine de caractères"
    print("Bonjour " + nom)


try:
    dire_bonjour("Alice")
    print(bonjour)
    dire_bonjour(24)
except AssertionError:
    print("Une erreur est survenue")
    print("Il s'agit d'une AssertionError")
except NameError:
    print("Une erreur est survenue")
    print("Il s'agit d'une NameError")


class MonTypeDErreur(Exception):
    pass

try:
    dire_bonjour("Alice")
    raise MonTypeDErreur("Pas bien")
    print(bonjour)
    dire_bonjour(24)
except AssertionError as e:
    print("Une erreur est survenue")
    print("Il s'agit d'une AssertionError")
    print(e)
except NameError as e:
    print("Une erreur est survenue")
    print("Il s'agit d'une NameError")
    print(e)
except MonTypeDErreur as e:
    print("Une erreur est survenue")
    print("Il s'agit d'une MonType")
    print(e)
print("FIN")