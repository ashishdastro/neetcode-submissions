class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
    
        # prereq -> course
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        q = deque()

        # courses with  no prerequisites
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)
        
        completed = 0
        while q:
            course = q.popleft()
            completed += 1

            # remove dependency on currently completed course
            for nei in graph[course]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)
        
        return completed == numCourses
