from assignment.assign import msa, frank_wolfe
from assignment.line import *
from assignment.graph import *
import time
# initialize the network

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

# True OD table:
#      3   4
# 1  200  150
# 2  140  185

# read from json
od_flow = {
    'N001': {'N003': 200, 'N004': 150},
    'N002': {'N003': 140, 'N004': 185}
}
origins = ['N001', 'N002']
destinations = ['N003', 'N004']


start_time = time.time()
vol1 = msa(nt, od_flow, origins, destinations)
for link in vol1.keys():
    print(vol1[link])
elapsed_time = time.time() - start_time
print('time of msa: ', elapsed_time)

start_time = time.time()
vol2 = frank_wolfe(nt, od_flow, origins, destinations)
for link in vol2.keys():
    print(vol2[link])
elapsed_time = time.time() - start_time
print('time of f-w: ', elapsed_time)
