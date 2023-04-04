# DFS algorithm in Python


# DFS algorithm
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


graph = {'1': set(['1', '2','3', '4','5', '6', '7', '8']),
         '2': set(['1', '2','3', '4','5', '6', '7', '8']),
         '3': set(['1', '2','3', '4','5', '6', '7', '8']),
         '4': set(['1', '2','3', '4','5', '6', '7', '8']),
         '5': set(['1', '2','3', '4','5', '6', '7', '8']),
         '6': set(['1', '2','3', '4','5', '6', '7', '8']),
         '7': set(['1', '2','3', '4','5', '6', '7', '8']),
         '8': set(['1', '2','3', '4','5', '6', '7', '8'])}

dfs(graph, '1')