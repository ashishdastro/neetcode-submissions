class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        state = [0] * numCourses

        def dfs(node):
            if state[node] == 1:
                return False # cycle
            
            if state[node] == 2:
                return True # already verified
            
            state[node] = 1

            for nei in graph[node]:
                if not dfs(nei):
                    return False
            
            state[node] = 2
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
        
 



