import heapq


class ShortestPath:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def dijkstra(net, source, sink):
        queue, checked = [(0, source, [])], set()
        while queue:
            (cost, v, path) = heapq.heappop(queue)
            if v not in checked:
                path = path + [v]
                checked.add(v)
                if v == sink:
                    return cost, path
                for pl in net.nodeset[v].heads:
                    heapq.heappush(queue, (cost+pl.cost, pl.pointee.id, path))

    @staticmethod
    def yen_kspp(net, source, sink, k):
        cost, spp = ShortestPath.dijkstra(net, source, sink)
        topk_pathset, paths, used, counter = [(cost, spp)], [spp], set(), 0
        for i in range(len(spp)-1):
            used.add((spp[i], spp[i+1]))
        # iteration
        for i in range(k-1):
            # get spurring and rooting nodes
            for j in range(len(paths[counter])-1):
                root = paths[counter][j]
                rootcost = 0
                if j != 0:
                    for r in range(j):
                        rootcost += net.edgefullset[(paths[counter][r], paths[counter][r+1])].cost
                for hedge in net.nodeset[root].heads:
                    # get spurpath and spur cost
                    n = hedge.pointee.id
                    if (root, n) not in used:
                        spurcost, spurpath = ShortestPath.dijkstra(net, n, sink)
                        pcost = rootcost+net.edgefullset[(root, n)].cost+spurcost
                        ppath = paths[counter][:j+1]+spurpath
                        topk_pathset.append((pcost, ppath))
                        for p in range(len(ppath) - 1):
                            used.add((ppath[p], ppath[p+1]))
        sortedpaths = sorted(topk_pathset)
        print(sortedpaths)
        if k > len(sortedpaths):
            print('wrong parameter, input a smaller k!')
        else:
            return sortedpaths[k-1]

