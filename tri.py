# Tri bulle
ma_liste = [3, 1, 15, 8, 12, 0]

# for i, val in ma_liste[:-1]:

for j in range(len(ma_liste) - 1):
    for i in range(len(ma_liste) - 1):
        if ma_liste[i] > ma_liste[i + 1]:
            # tmp = ma_liste[i]
            # ma_liste[i] = ma_liste[i+1]
            # ma_liste[i+1] = tmp
            ma_liste[i], ma_liste[i + 1] = ma_liste[i + 1], ma_liste[i]

print(ma_liste)




def fusion(liste_1: list, liste_2: list) -> list:
    """
    Fusionne deux listes déjà triées en une liste triée
    :param liste_1: une liste triée
    :param liste_2: une autre liste triée
    :return:
    """
    resultat = []
    i, j = 0, 0

    while i < len(liste_1) and j < len(liste_2):
        if liste_1[i] < liste_2[j]:
            resultat.append(liste_1[i])
            i += 1
        else:
            resultat.append((liste_2[j]))
            j += 1
    resultat.extend(liste_2[j:])
    resultat.extend(liste_1[i:])
    return resultat

print(fusion([2,6,7], [0,1,12]))


def tri_fusion(arr):
    """
    Tri fusion d'une liste
    :param arr:
    :return:
    """
    # Si la taille de la liste est égale à 0 ou 1 on renvoir directment la liste
    if len(arr) < 2:
        return arr
    # Si la taille de la liste est égale à 2 on inverse la liste si nécessaire
    elif len(arr) == 2:
        return arr if arr[0] < arr[1] else arr[::-1]
    # Dans les autres cas on divise la liste en deux
    else:
        arr1 = arr[:len(arr)//2]
        arr2 = arr[len(arr)//2:]

        arr1_sorted = tri_fusion(arr1)
        arr2_sorted = tri_fusion(arr2)
    return fusion(arr1_sorted, arr2_sorted)
