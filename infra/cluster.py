# from .node import Node
from infra.node import Node


class ClusterCapacityOverflow(Exception):
    pass


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
