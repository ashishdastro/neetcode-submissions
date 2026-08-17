class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        q = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)
        
        order = []
        while q:
            course = q.popleft()
            order.append(course)

            for nei in graph[course]:
                indegree[nei] -= 1
                
                if indegree[nei] == 0:
                    q.append(nei)
        
        return order if len(order) == numCourses else []
