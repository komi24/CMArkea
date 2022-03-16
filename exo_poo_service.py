import yaml


class Service:
    """
    attrs:
    - host
    - environment
    - service
    - ip
    methods:
    - get_dict() -> dict
    - generate_yaml() -> str
    - generate_yaml_file(filename)
    """
    def __init__(
        self,
        host: str,
        environment: str,
        service: str,
        ip: str = None,
        concurrency:int = 1
    ):
        self.host = host
        self.environment = environment
        self.service = service
        self.ip = ip
        self.concurrency = concurrency

    def get_dict(self) -> dict:
        return {
            "host": self.host,
            "environment": self.environment,
            "service": self.service,
            "ip": self.ip,
            "concurrency": self.concurrency
        }

    def generate_yaml_file(self, filename) -> dict:
        with open(filename, "w") as file:
            yaml.dump(self.get_dict(), file)



class CapacityOverflow(Exception):
    pass

sum([1,2,1,1])


class Node:
    """
    attrs:
    - name
    - capacity
    - service_list
    methods:
    - add_service(service) ajoute un service dans le node si capacity le permet
    """
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.service_list = []

    def add_service(self, service):
        print(service.concurrency)
        print(self.service_list[0].concurrency)
        total_concurrency = 0
        for serv in self.service_list:
            total_concurrency += serv.concurrency
            
        # self.service_list.append(service)






node1 = Node()
node1.add_service()


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