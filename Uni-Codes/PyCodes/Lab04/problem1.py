from queue import PriorityQueue
import math

file = open("input1.txt", "r")
output = open("output1.txt", "w")
test_cases = file.readline()


def Dijkstra(graph, source):
    sizeOfGraph = len(graph)
    dist = [math.inf]*sizeOfGraph
    prev = [None]*sizeOfGraph
    dist[source] = 0

    Q = PriorityQueue()

    visited = [False]*sizeOfGraph
    Q.put((dist[source], source))

    for vertex in graph:
        if vertex != source:
            dist[vertex] = math.inf
            prev[vertex] = None

        Q.put((dist[source], source))
        visited[vertex] = False

    while not Q.empty():
        u = Q.get()[1]

        if visited[u]:
            continue

        visited[u] = True

        for v in graph[u]:
            alt = dist[u] + v[1]

            if alt < dist[v[0]]:
                dist[v[0]] = alt
                prev[v[0]] = u
                Q.put((dist[v[0]], v[0]))

    return dist[sizeOfGraph - 1]


adjList = {}

for i in range(int(test_cases)):

    lists = file.readline().split()

    N = int(lists[0])
    M = int(lists[1])

    for i in range(N+1):
        adjList[i] = []

    for i in range(M):
        l2 = file.readline().split()
        u = int(l2[0])
        v = int(l2[1])
        w = int(l2[2])
        adjList[u].append([v, w])

    print(Dijkstra(adjList, 1), file=output)
