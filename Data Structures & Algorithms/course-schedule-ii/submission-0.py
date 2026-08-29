class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        crsToPre = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            crsToPre[crs].append(pre)
        
        output = []
        visited, cycle = set(), set()

        def dfs(crs):
            if crs in visited:
                return True
            
            if crs in cycle:
                return False
            
            cycle.add(crs)
            for pre in crsToPre[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return output