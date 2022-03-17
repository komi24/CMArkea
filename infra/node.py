

class CapacityOverflow(Exception):
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

