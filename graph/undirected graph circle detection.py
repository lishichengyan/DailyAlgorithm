"""
以下的算法基于邻接表，思想是深度优先搜索，如果发现某个节点的某个邻居之前已经被访问过，但这个节点又不是当前节点的父亲，就说明有环
"""
def dfs(graph, src, visited, parent):
    visited[src] = 1
    for nei in graph[src]:
        if visited[nei] == 0:
            if dfs(graph, nei, visited, src):
                return True
        elif nei != parent:
            return True
    return False
