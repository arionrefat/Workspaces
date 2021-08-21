from queue import PriorityQueue
import math

input = open("input4.txt", "r")
output = open("output4.txt", "w")
test_cases = input.readline()


def Network(graph, source):
    sizeOfGraph = len(graph)
    dist = [-math.inf]*(sizeOfGraph+1)
    dist[source] = math.inf
    Q = PriorityQueue()

    visited = [False]*(sizeOfGraph+1)

    for vertex in graph:
        Q.put((-dist[vertex], vertex))

    while not Q.empty():
        u = Q.get()[-1]

        if visited[u]:
            continue

        visited[u] = True

        for vertex in graph[u]:
            alt = min(dist[u], vertex[1])

            if alt > dist[vertex[0]]:
                dist[vertex[0]] = alt
                Q.put((-dist[vertex[0]], vertex[0]))

    for i in range(1, sizeOfGraph):
        if dist[i] == -math.inf:
            dist[i] = -1
    dist[source] = 0
    print(*dist[1:], file=output)


adjList = {}

for i in range(int(test_cases)):
    lists = input.readline().split()

    N = int(lists[0])
    M = int(lists[1])

    for i in range(1, N + 1):
        adjList[i] = []

    for j in range(M):
        anotherList = input.readline().split()
        u = int(anotherList[0])
        v = int(anotherList[1])
        w = int(anotherList[2])
        adjList[u].append([v, w])

    source = int(input.readline())
    Network(adjList, source)
