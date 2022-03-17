def en_majuscule(f_originale):
    print("Décoration")
    def nouvelle_fonction(*args, **kwargs):
        print("exec")
        nouveaux_args = [arg.upper() for arg in args]
        nouveaux_kwargs = {
            key: val.upper()
            for key, val in kwargs.items()
        }
        return f_originale(*nouveaux_args, **nouveaux_kwargs)
    return nouvelle_fonction


@en_majuscule
def dire_bonjour(nom, prenom, ville="Brest"):
    print(f"Bonjour {prenom} {nom}. J'habite à {ville}.")

print("Start")
dire_bonjour("Terrier", "Martin", ville="Rennes")
dire_bonjour("Terriere", "Martine", ville="Rennes")
