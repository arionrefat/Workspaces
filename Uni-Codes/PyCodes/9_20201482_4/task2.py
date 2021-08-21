from queue import PriorityQueue
import math

input = open("input2.txt", "r")
output = open("output2.txt", "w")
test_cases = input.readline()


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

        for vertex in graph[u]:
            alt = dist[u] + vertex[1]

            if alt < dist[vertex[0]]:
                dist[vertex[0]] = alt
                prev[vertex[0]] = u
                Q.put((dist[vertex[0]], vertex[0]))
    set = []
    index = len(prev)-1

    while(1):
        if prev[index] == None:
            set.append(1)
            break

        set.append(index)
        index = prev[index]
    set.reverse()
    print(*set, file=output)


adjacentList = {}

for i in range(int(test_cases)):

    lists = input.readline().split()

    N = int(lists[0])
    M = int(lists[1])

    for i in range(N+1):
        adjacentList[i] = []

    for j in range(M):
        anotherList = input.readline().split()
        u = int(anotherList[0])
        v = int(anotherList[1])
        w = int(anotherList[2])
        adjacentList[u].append([v, w])

    Dijkstra(adjacentList, 1)
