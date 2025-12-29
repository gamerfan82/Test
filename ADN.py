import random


graph = {
    'A': {'B': 4, 'C': 3},
    'B': {'A': 4, 'D': 5, 'E': 2},
    'C': {'A': 3, 'D': 6, 'F': 4},
    'D': {'B': 5, 'C': 6, 'G': 3},
    'E': {'B': 2, 'G': 4, 'H': 6},
    'F': {'C': 4, 'G': 2},
    'G': {'D': 3, 'E': 4, 'F': 2, 'H': 3},
    'H': {'E': 6, 'G': 3}
}
#graph = {
#     'A': {'B': 3, 'C': 4},
#     'B': {'A': 3, 'D': 2, 'E': 5},
#     'C': {'A': 4, 'F': 3},
#     'D': {'B': 2, 'G': 3},
#     'E': {'B': 5, 'G': 4, 'H': 6},
#     'F': {'C': 3, 'H': 5},
#     'G': {'D': 3, 'E': 4, 'I': 2},
#     'H': {'E': 6, 'F': 5, 'I': 3},
#     'I': {'G': 2, 'H': 3, 'J': 4},
#     'J': {'I': 4}
# }


pheromone = {}
for n in graph:
    for i in graph[n]:
        pheromone[(n, i)] = 1.0

#tasire pheromone
alpha = 1.0
#tasire distance
beta = 2.0
ants = 10
loop = 20

def choose_next_node(current, visited):
    list_node = []
    total = 0

    for hamsaye in graph[current]:
        if hamsaye not in visited:
            tau = pheromone[(current, hamsaye)]
            eta = 1 / graph[current][hamsaye]
            value = (tau ** alpha) * (eta ** beta)
            list_node.append((hamsaye, value))
            total += value


    r = random.uniform(0, total)
    upto = 0
    for node, value in list_node:
        upto += value
        if upto >= r:
            return node

best_path = None
best_length = 9999

for x in range(loop):
    all_paths = []

    for ys in range(ants):
        path = ['A']
        visited = set(path)
        length = 0
        current = 'A'

        while current != 'H':
            next_node = choose_next_node(current, visited)
            if next_node is None:  
                break
            length += graph[current][next_node]
            path.append(next_node)
            visited.add(next_node)
            current = next_node

        all_paths.append((path, length))

        if length < best_length:
            best_length = length
            best_path = path

    for j in pheromone:
        pheromone[j] *= 0.5

    for path, length in all_paths:
        for i in range(len(path) - 1):
            pheromone[(path[i], path[i + 1])] += 1 / length

print("Best Path:", best_path)
print("Path Length:", best_length)
