import yaml

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


liste_configs = [conf for conf in build_all_configs(10)]

# liste_configs = []
# for conf in build_all_configs(10):
#     liste_configs.append(conf)

# liste_pers = [{"prenom": "Mickael", "nom": "Bolnet"}]
with open("config.yaml", "w") as fichier:
    yaml.dump(liste_configs, fichier)


