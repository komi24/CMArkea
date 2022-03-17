# from mon_package import mon_module
# from mon_package.mon_module import dire_bonjour
from mon_package import dire_bonjour
from infra import Node, Cluster, Service


# mon_module.dire_bonjour()
# dire_bonjour()
# dire_bonjour()

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

