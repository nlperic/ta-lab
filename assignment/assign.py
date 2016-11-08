from copy import deepcopy
from assignment.line import *
from assignment.shortest_path import ShortestPath as SPP


# True OD table:
    #      3   4
    # 1  200  150
    # 2  140  185

# od_flow = {
    #     'N001': {'N003': 200, 'N004': 150},
    #     'N002': {'N003': 140, 'N004': 185}
    # }
# origins = ['N001', 'N002']
# destinations = ['N003', 'N004']


def frank_wolfe(network, od_flow, origins, destinations):
    network.init_cost()
    # empty volume, for update volume and potential volume
    empty = {}
    for l in network.edge_id_set:
        empty[l] = 0

    potential_volume = deepcopy(empty)

    # initial all-or-nothing assignment
    for o in origins:
        for d in destinations:
            cost, path = SPP.dijkstra(network, o, d)
            lpath = [network.edgenode[(path[i], path[i + 1])] for i in range(len(path) - 1)]
            for l in lpath:
                potential_volume[l] += od_flow[o][d]
    # x_1 = M(c_0)
    volume = deepcopy(potential_volume)
    potential_volume = deepcopy(empty)
    temp_vol = deepcopy(empty)
    step = 1
    while cal_limit(volume, temp_vol) > 0.5 and step > 0.0005:
        network.update_cost(volume)
        temp_vol = deepcopy(volume)
        for o in origins:
            for d in destinations:
                cost, path = SPP.dijkstra(network, o, d)
                lpath = [network.edgenode[(path[i], path[i + 1])] for i in range(len(path) - 1)]
                for l in lpath:
                    potential_volume[l] += od_flow[o][d]
        step = cal_step(network, volume, potential_volume)
        for link in network.edge_id_set:
            volume[link] += step * (potential_volume[link] - volume[link])
        potential_volume = deepcopy(empty)
    return volume


def msa(network, od_flow, origins, destinations):
    network.init_cost()
    # empty volume, for update volume and potential volume
    empty = {}
    for l in network.edge_id_set:
        empty[l] = 0

    volume = deepcopy(empty)
    potential_volume = deepcopy(empty)

    # initial all-or-nothing assignment
    for o in origins:
        for d in destinations:
            cost, path = SPP.dijkstra(network, o, d)
            lpath = [network.edgenode[(path[i], path[i + 1])] for i in range(len(path) - 1)]
            for l in lpath:
                potential_volume[l] += od_flow[o][d]
    # x_1 = M(c_0)
    volume = deepcopy(potential_volume)
    potential_volume = deepcopy(empty)
    temp_vol = deepcopy(empty)
    n = 1
    while cal_limit(volume, temp_vol) > 0.5:
        n += 1
        network.update_cost(volume)
        temp_vol = deepcopy(volume)
        for o in origins:
            for d in destinations:
                cost, path = SPP.dijkstra(network, o, d)
                lpath = [network.edgenode[(path[i], path[i + 1])] for i in range(len(path) - 1)]
                for l in lpath:
                    potential_volume[l] += od_flow[o][d]
        for link in network.edge_id_set:
            volume[link] = (1-1/n) * volume[link] + 1/n * potential_volume[link]
        potential_volume = deepcopy(empty)
    return volume
    