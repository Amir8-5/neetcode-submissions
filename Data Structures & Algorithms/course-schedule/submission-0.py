class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        crsToPre = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            crsToPre[crs].append(pre)
        
        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            
            if crsToPre[crs] == []:
                return True
            
            visited.add(crs)
            for pre in crsToPre[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            crsToPre[crs] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
