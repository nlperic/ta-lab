def objective(net, volumes):
    total = 0
    for lid in volumes.keys():
        cost = net.edgeset[lid].cal_weight(volumes[lid])
        total += cost
    return total


def div(net, prior, posterior, step):
    idiv = 0
    for lid in prior.keys():
        dist = posterior[lid] - prior[lid]
        cost = dist*net.edgeset[lid].cal_weight(prior[lid] + step * dist)
        idiv += cost
    return idiv


def cal_step(net, prior, posterior):
    lb = 0.0
    ub = 1.0
    step = (lb + ub) / 2.0
    while abs(div(net, prior, posterior, step)) >= 0.01 and abs(ub-lb) > 0.001:
        if div(net, prior, posterior, step) * div(net, prior, posterior, ub) > 0:
            ub = step
        else:
            lb = step
        step = (lb + ub) / 2.0
    return step


def cal_limit(prior, posterior):
    limiter = 0
    for l in prior:
        limiter += abs(prior[l]-posterior[l])
    return limiter