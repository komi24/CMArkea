from infrastructure import Node, Cluster, Service
import argparse


parser = argparse.ArgumentParser(
    description="Tool to deploy a cluster"
)
parser.add_argument(
    "filename", help="input description yaml file for our infrastructure")
parser.add_argument("--output", help="ouptut log file")
args = parser.parse_args()

node1 = Node("Node 1", 2, "189.178.1.1")
node2 = Node("Node 2", 10, "189.178.1.2")
cluster = Cluster()
cluster.add_node(node1)
cluster.add_node(node2)

cluster.add_service(Service("mydb.com", "prod", "website"))
cluster.add_service(Service("mydb.com", "preprod", "website", concurrency=4))
cluster.add_service(Service("db.mydb.com", "prod", "db"))

cluster.generate_yaml(args.output)
