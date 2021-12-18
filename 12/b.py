with open("input.txt") as inp:
    graph = {}
    for line in inp:
        node1, node2 = line.strip().split('-')
        if node1 not in graph:
            graph[node1] = [node2]
        else:
            graph[node1].append(node2)

        if node2 not in graph:
            graph[node2] = [node1]
        else:
            graph[node2].append(node1)

print(graph)

def count_paths(start, end, visited, visited_twice):
    if start == "start" and start in visited:
        return 0
    elif start == end:
        return 1
    else:
        if start.lower() == start:
            if start in visited:
                if visited_twice:
                    return 0
                else:
                    visited_twice = True
            visited = visited | frozenset([start])
        return sum(count_paths(child, end, visited, visited_twice) for child in graph[start])

print(count_paths("start", "end", frozenset(), False))