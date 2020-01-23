# 785. Is Graph Bipartite?
# https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        NOT_EXPLORED, RED, BLUE = -1, 0, 1
        color = [NOT_EXPLORED]*n
        for u in range(n):
            if color[u] == NOT_EXPLORED:
                color[u] = RED
                stack = []
                stack.append(u)
                while stack:
                    curr = stack.pop()
                    for v in graph[curr]:
                        if color[v] == NOT_EXPLORED:
                            color[v] = BLUE if color[curr] == RED else RED
                            stack.append(v)
                        elif color[curr] == color[v]:
                            return False
        return True
