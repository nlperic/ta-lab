from assignment.graph import *
from assignment.shortest_path import ShortestPath as SPP

nt = Network('net')
node = Vertex("a")

# read from csv
with open('network.csv') as fo:
    lines = fo.readlines()
    for ln in lines:
        eg = ln.split(',')
        nt.add_edge(Edge(eg))
# initialize cost
nt.init_cost()
o, d = 'N001', 'N004'
cost, path = SPP.yen_kspp(nt, o, d, 2)
print(cost)
