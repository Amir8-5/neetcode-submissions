class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        visit = set()
        nei = [[] for _ in range(n)]
        for x, y in edges:
            nei[x].append(y)
            nei[y].append(x)
        

        def dfs(node, par):
            if node in visit:
                return False
            visit.add(node)
            for n in nei[node]:
                if n == par:
                    continue
                
                if not dfs(n, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visit) == n

            
