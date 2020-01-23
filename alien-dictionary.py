# 269. Alien Dictionary
# https://leetcode.com/problems/alien-dictionary/

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        from collections import defaultdict

        def build_graph(words):
            graph = defaultdict(set)
            indegree = dict()

            for word in words:
                for c in word:
                    indegree[c] = 0
            
            for i in range(len(words)-1):
                w1, w2 = words[i], words[i+1]
                length = min(len(w1), len(w2))
                for j in range(length):
                    c1, c2 = w1[j], w2[j]
                    if c1 != c2:
                        graph[c1].add(c2)
                        break
            
            for (u, neighbors,) in graph.items():
                for v in neighbors:
                    indegree[v] += 1
                    
            return (graph, indegree,)
                
                
        def topological_traversal(graph):
            g = graph[0]
            indegree = graph[1]
            
            ans = []
            queue = []
            
            for (u, k,) in indegree.items():
                if k == 0:
                    queue.append(u)
            
            while queue:
                u = queue.pop(0)
                ans.append(u)
                for v in g[u]:
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        queue.append(v)
            
            return ''.join(ans) if len(ans) == len(indegree) else ''

        g = build_graph(words)
        return topological_traversal(g)
