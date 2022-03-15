"""
Faire une fonction qui permet de contruire un serveur (host, port, ip) sous un dico
Faire une fonction qui permet de contruire une liste de serveurs
faire un print de la liste de serveurs
"""

def build_server():
    host = input("Quel est votre host ?")
    port = int(input("Quel est votre port ?"))
    ip = input("Quel est votre ip ?")
    return {
        "host": host,
        "port": port,
        "ip": ip,
    }


def add_unique_server(liste_serv: list, new_serv):
    serv = new_serv
    while (serv["port"], serv["host"]) in [(s["port"], s["host"]) for s in liste_serv]:
        serv["port"] += 1
    liste_serv.append(serv)

def add_unique_server(liste_serv: list, new_serv):
    serv = new_serv
    is_duplicated = True
    while is_duplicated:
        for current_server in liste_serv:
            if current_server["host"] == serv["host"] and current_server["port"] == serv["port"]:
                is_duplicated = True
                serv["port"] += 1
            else:
                is_duplicated = False
    liste_serv.append(serv)


def build_config():
    response = "o"
    liste_serveurs = []
    while response.lower() == "o":
        new_serv = build_server()
        add_unique_server(liste_serveurs, new_serv)
        response = input("Voulez-vous ajouter un serveur ? o/n")
    return liste_serveurs

# res = build_config()
# print(res)


# events = {
#     "click": click_handler,
#     "hover": hover_handler,
#     "delete": delete_handler
# }
#
#
# event = "click"
# events[event]()


ma_variable = 0

def ma_fonction():
    print(ma_variable)
    ma_variable = 5
    print(ma_variable)

print(ma_variable)
ma_fonction()
print(ma_variable)