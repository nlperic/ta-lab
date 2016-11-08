import numpy as np


class Edge:
    def __init__(self, edge_info):
        self.id = edge_info[0]
        self.pointer = Vertex(edge_info[1])
        self.pointee = Vertex(edge_info[2])
        self.fft = float(edge_info[3])
        self.capacity = float(edge_info[4])
        self.alpha = float(edge_info[5])
        self.beta = float(edge_info[6].strip())
        self.cost = float('inf')
        self.volume = 0

    # def __init__(self, edge_id, prec, post, free_flow_time, dividend, multiplier=0.15, power=4.0):
    #     self.id = edge_id
    #     self.pointer = Vertex(prec)
    #     self.pointee = Vertex(post)
    #     self.fft = free_flow_time
    #     self.capacity = dividend
    #     self.alpha = multiplier
    #     self.beta = power
    #     self.cost = float('inf')
    #     self.volume = 0

    # calculate the weight by BPR function:
    def cal_weight(self, volume):
        self.cost = self.fft*(1+self.alpha*np.power(volume/self.capacity, self.beta))
        return self.cost

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.pointer.id == other.pointer.id) and (self.pointee.id == other.pointee.id)
        else:
            return False


class Vertex:
    def __init__(self, node_id):
        self.id = node_id
        self.tails = []
        self.heads = []
        self.prev = None
        self.potential = float('inf')

    def __cmp__(self, other):
        return __cmp__(self.potential, other.potential)


class Network:
    def __init__(self, netname):
        self.name = netname
        self.edge_id_set = set()
        self.edgeset = {}
        self.edgefullset={}
        self.edgenode = {}
        self.node_id_set = set()
        self.nodeset = {}

    def add_edge(self, edge):
        self.edge_id_set.add(edge.id)
        self.edgeset[edge.id] = edge
        self.edgefullset[(edge.pointer.id,edge.pointee.id)] = edge
        self.edgenode[(edge.pointer.id, edge.pointee.id)] = edge.id
        if edge.pointer.id not in self.node_id_set:
            node = Vertex(edge.pointer)
            node.heads.append(edge)
            self.nodeset[edge.pointer.id] = node
            self.node_id_set.add(edge.pointer.id)
        else:
            self.nodeset[edge.pointer.id].heads.append(edge)
        if edge.pointee.id not in self.node_id_set:
            node = Vertex(edge.pointee)
            node.tails.append(edge)
            self.nodeset[edge.pointee.id] = node
            self.node_id_set.add(edge.pointee.id)
        else:
            self.nodeset[edge.pointee.id].tails.append(edge)

    def init_cost(self):
        volume = {}
        for l in self.edge_id_set:
            volume[l] = 0
        self.update_cost(volume)

    def update_cost(self, volume):
        for l in self.edgeset.keys():
            self.edgeset[l].cal_weight(volume[l])
