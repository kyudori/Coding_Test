import heapq  
  
def dijkstra(graph, start, end):  
    distance = [INF] * (n+1)  
    q = []  
    heapq.heappush(q, (0, start))  
    distance[start] = 0  
    while q:  
        # print(q)  
        dist, now_node = heapq.heappop(q)  
  
        if dist > distance[now_node]:  
            continue  
  
        for i in graph[now_node]:  
            cost = i[0] + dist  
  
            if cost < distance[i[1]]:  
                distance[i[1]] = cost  
                heapq.heappush(q, (distance[i[1]], i[1]))
    # print(graph)  
    # print(distance)
    return distance[end]  
  
n, m = list(map(int, input().split()))  
  
graph = [[] for _ in range(n+1)]  
INF = 1e9  
  
for i in range(1, m+1):  
    a, b = list(map(int, input().split()))  
  
    graph[a].append((1, b))  
    graph[b].append((1, a))  
  
x, k = list(map(int, input().split()))  
  
answer = dijkstra(graph, 1, k) + dijkstra(graph, k, x)  
  
if answer >= INF:  
    print("-1")  
else:  
    print(answer)