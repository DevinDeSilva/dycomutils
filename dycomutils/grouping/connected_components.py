def findParent(parent, x):
    if parent[x] == x:
        return x

    parent[x] = findParent(parent, parent[x])
    return parent[x]


def unionSets(parent, x, y):
    px = findParent(parent, x)
    py = findParent(parent, y)
    if px != py:
        parent[px] = py


def getComponents(V, edges):
    parent = [i for i in range(V)]

    for edge in edges:
        unionSets(parent, edge[0], edge[1])

    for i in range(V):
        parent[i] = findParent(parent, i)

    resMap = {}
    for i in range(V):
        root = parent[i]
        if root not in resMap:
            resMap[root] = []
        resMap[root].append(i)

    res = list(resMap.values())

    return res
