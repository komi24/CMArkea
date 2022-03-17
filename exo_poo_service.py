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

    def __repr__(self):
        return f"Sevice -> host : {self.host}, service: {self.service}, env: {self.environment}"

class CapacityOverflow(Exception):
    pass

class ClusterCapacityOverflow(Exception):
    pass


class Node:
    """
    attrs:
    - name
    - capacity
    - service_list
    methods:
    - add_service(service) ajoute un service dans le node si capacity le permet
    """
    def __init__(self, name, capacity, ip):
        self.name = name
        self.ip = ip
        self.remaining_capacity = capacity
        self.total_capacity = capacity
        self.service_list = []

    def add_service(self, service):
        """
        Modifier add service pour verifier si il nous reste assez de capacity dans le node
        :param service:
        :return:
        """
        if self.remaining_capacity >= service.concurrency:
            service.ip = self.ip
            self.service_list.append(service)
            self.remaining_capacity -= service.concurrency
        else:
            raise CapacityOverflow()

    def has_remaining_capacity(self, minimum_capacity_to_have) -> bool:
        return self.remaining_capacity >= minimum_capacity_to_have

    def __repr__(self):
        return f"Node: {self.name}, remaining: {self.remaining_capacity}, " +\
            f"services : {self.service_list}"


class Cluster:
    """
    attrs:
    - node_list
    methods:
    - add_node(node)
    - add_service(service) # rajouter un service dans le premier node libre
    """
    def __init__(self):
        self.node_list: list[Node] = []

    def add_node(self, node: Node):
        self.node_list.append(node)

    def add_service(self, service):
        is_service_added = False
        for node in self.node_list:
            if node.has_remaining_capacity(service.concurrency):
                node.add_service(service)
                is_service_added = True
                break
        if not is_service_added:
            raise ClusterCapacityOverflow()


node1 = Node("Node 1", 2, "189.178.1.1")
node2 = Node("Node 2", 10, "189.178.1.2")
cluster = Cluster()
cluster.add_node(node1)
cluster.add_node(node2)

cluster.add_service(Service("mydb.com", "prod", "website"))
cluster.add_service(Service("mydb.com", "preprod", "website", concurrency=4))
cluster.add_service(Service("db.mydb.com", "prod", "db"))

# node1.add_service(Service("mydb.com", "prod", "website"))
# node1.add_service(Service("mydb.com", "preprod", "website", concurrency=4))
print(node1)
print(node2)



# def build_config(n, host, ip_suffix, environment, service):
#     for i in range(1, n+1):
#         yield {
#             "host": host,
#             "environment": environment,
#             "service": service,
#             "ip": ip_suffix + str(i),
#         }
#
#
# def build_all_configs(n):
#     host_list = ["mydb.com", "data.mydb.com", "ppe.mydb.com", "ppe.data.mydb.com"]
#     ip_suffix_list = ["189.175.1.", "189.175.2.", "189.175.3.", "189.175.4."]
#     service_list = ["website", "data services", "website", "data services"]
#     environment_list = ["prod", "prod", "ppe", "ppe"]
#     for host, ip_suffix, service, environment in zip(host_list, ip_suffix_list, service_list, environment_list):
#         gen = build_config(n, host, ip_suffix, environment, service)
#         for conf in gen:
#             yield conf
#
#
# liste_configs = [conf for conf in build_all_configs(10)]

