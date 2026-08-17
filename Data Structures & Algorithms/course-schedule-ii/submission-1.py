class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            graph[prereq].append(course)

        state = [0] * numCourses
        order = []

        def dfs(course):
            # Found cycle
            if state[course] == 1:
                return False

            # Already completely processed
            if state[course] == 2:
                return True

            # Mark as currently exploring
            state[course] = 1

            for nei in graph[course]:
                if not dfs(nei):
                    return False

            # Finished exploring this node
            state[course] = 2
            order.append(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return order[::-1]