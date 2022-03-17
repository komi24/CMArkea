# Packing vs Unpacking

def dire_bonjour(*args, **kwargs):
    print(args)
    print(kwargs)


dire_bonjour("Martin", "Olivier", name="Jeane", ville="Brest")


def dire_bonjour(prenom, nom, ville="Brest"):
    print(f"Bonjour {prenom} {nom}. J'habite à {ville}")


liste_arg = ["Mathieu", "Alaphilipe", "Lyon"]
dire_bonjour(*liste_arg)

liste_arg = ["Mathieu"]
dic = {"nom": "Alaphilipe", "ville": "Lyon"}
dire_bonjour(*liste_arg, **dic)

type(**dic)
# Decorateurs
