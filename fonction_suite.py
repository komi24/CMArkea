def generatrice(n):
    while n > 0:
        yield n
        yield n + 4
        n -= 1

# for i in generatrice(4):
#     print(i)
#
# for i in generatrice(5):
#     print(i)

a = generatrice(5)
print("premier tour")
for i in a:
    print(i)

print("deuxieme tour")
for i in a:
    print(i)
print("fin")

print(range(10))
print([i*2 for i in range(10)])

# Faire une fonction generatrice qui prend n en paramètre et renvoie les nombres de 0 à n
# dans l'ordre croissant

# #
# host, ip, environment, service
# mydb.com, 189.175.1.1-n, prod, website
# data.mydb.com, 189.175.2.1-n, prod, data services
# ppe.mydb.com, 189.175.3.1-n, ppe, website
# ppe.data.mydb.com, 189.175.4.1-n, ppe, data services
{"host": "mydb.com", "ip": "189.175.1.1", "environment": "prod", "service": "website"}
{"host": "mydb.com", "ip": "189.175.1.2", "environment": "prod", "service": "website"}

def build_config(n, host, ip_suffix, environment, service):
    for i in range(1, n+1):
        yield {
            "host": host,
            "environment": environment,
            "service": service,
            "ip": ip_suffix + str(i),
        }

def build_all_configs(n):
    host_list = ["mydb.com", "data.mydb.com", "ppe.mydb.com", "ppe.data.mydb.com"]
    ip_suffix_list = ["189.175.1.", "189.175.2.", "189.175.3.", "189.175.4."]
    service_list = ["website", "data services", "website", "data services"]
    environment_list = ["prod", "prod", "ppe", "ppe"]
    for host, ip_suffix, service, environment in zip(host_list, ip_suffix_list, service_list, environment_list):
        gen = build_config(n, host, ip_suffix, environment, service)
        for conf in gen:
            yield conf

def build_all_configs_2(n):
    host_list = ["mydb.com", "data.mydb.com", "ppe.mydb.com", "ppe.data.mydb.com"]
    ip_suffix_list = ["189.175.1.", "189.175.2.", "189.175.3.", "189.175.4."]
    service_list = ["website", "data services", "website", "data services"]
    environment_list = ["prod", "prod", "ppe", "ppe"]

    liste_gen = []
    for host, ip_suffix, service, environment in zip(host_list, ip_suffix_list, service_list, environment_list):
        liste_gen.append(build_config(n, host, ip_suffix, environment, service))

    for i in range(n):
        for gen in liste_gen:
            yield next(gen)

# for conf in build_config(5, "mydb.com", "189.175.1.", "prod", "website"):
#     print(conf)


# iterator = build_config(5, "mydb.com", "189.175.1.", "prod", "website")

# print(next(build_config(5, "mydb.com", "189.175.1.", "prod", "website")))
# print(next(build_config(5, "mydb.com", "189.175.1.", "prod", "website")))

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

with open("mon_fichier.txt", "a") as file:
    file.write("Bonjour")

import os, sys, shutil
print(os.listdir())

if not os.path.exists("mon_repertoire"):
    os.mkdir("mon_repertoire")

shutil.copy("mon_fichier.txt", "ma_copie.txt")

import json


with open("mon_fichier.json", "w") as fichier:
    liste_pers = [{"prenom": "Mickael", "nom": "Bolnet"}]
    print(json.dumps(liste_pers))
    json.dump(liste_pers, fichier, indent=2, sort_keys=True)


