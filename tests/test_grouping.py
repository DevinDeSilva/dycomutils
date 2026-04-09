from dycomutils.grouping import findParent, getComponents, unionSets


def test_union_sets_and_find_parent():
    parent = [0, 1, 2, 3]

    unionSets(parent, 0, 1)
    unionSets(parent, 1, 2)

    assert findParent(parent, 0) == findParent(parent, 2)
    assert findParent(parent, 3) != findParent(parent, 0)


def test_get_components_returns_connected_groups():
    components = getComponents(6, [(0, 1), (1, 2), (3, 4)])

    normalized = sorted(sorted(component) for component in components)

    assert normalized == [[0, 1, 2], [3, 4], [5]]
