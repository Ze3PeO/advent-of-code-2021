def p1(inp):
    global visited, graph, path, count
    graph = inp
    path = []
    count = 0
    visited = {}

    for key in graph.keys():
        visited[key] = False

    find_all_paths_dfs_p1('start', 'end')

    return count


def find_all_paths_dfs_p1(node, dest):
    global count
    visited[node] = True
    path.append(node)

    if node == dest:
        count += 1
    else:
        for child in graph[node]:
            if not visited[child] or any(c.isupper() for c in child):
                find_all_paths_dfs_p1(child, dest)

    path.pop()
    visited[node] = False


def p2(inp):
    return 0
'''
#-------------------------------------------------------------------------------
# Eigener Lösungsansatz:
# (Funktioniert nicht richtig)
#-------------------------------------------------------------------------------

    global visited, graph, path, count
    graph = inp
    path = []
    count = 0
    visited = {}

    for key in graph.keys():
        visited[key] = 0

    find_all_paths_dfs_p2('start', 'end')

    return count


def find_all_paths_dfs_p2(node, dest):
    global count
    visited[node] += 1
    path.append(node)

    if node == dest:
        count += 1
    else:
        for child in graph[node]:
            if child == 'start' and not visited[child] >= 1:
                find_all_paths_dfs_p2(child, dest)
                continue

            if any(c.isupper() for c in child):
                find_all_paths_dfs_p2(child, dest)
                continue

            amount = 0
            for value in visited.values():
                if value >= 2:
                    amount += 1
            if not visited[child] >= 2 and amount <= 1:
                find_all_paths_dfs_p2(child, dest)
                continue

    path.pop()
    visited[node] -= 1
'''


with open('../../input/week2/day12.txt') as file:
    inp = {}
    for line in file.readlines():
        split = line.strip().split("-")
        if split[0] not in inp:
            inp[split[0]] = []

        inp[split[0]].append(split[1])
        if split[1] not in inp:
            inp[split[1]] = []
        inp[split[1]].append(split[0])

    print('part 1: ' + str(p1(inp)))
    print('part 2: ' + str(p2(inp)))
