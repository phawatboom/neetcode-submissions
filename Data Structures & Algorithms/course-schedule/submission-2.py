from collections import deque

# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
#         graph = {i:[] for i in range(numCourses)}
#         indegree = [0] * numCourses

#         for course, prereq in prerequisites:
#             graph[prereq].append(course)
#             indegree[course] += 1

#         # loop through all teh courses to find courses without prerequisites]
#         queue = deque()
#         for i in range(numCourses):
#             if indegree[i] == 0:
#                 queue.append(i)

#         completed = 0
#         while queue:
#             node = queue.popleft()
#             completed += 1
#             for neighbor in graph[node]:
#                 indegree[neighbor] -= 1
#                 if indegree[neighbor] == 0:
#                     queue.append(neighbor)
#         return completed == numCourses

# backtracking version

class Solution:
    def canFinish(self, numCourses, prerequisites):
        # 1. Construct adjacency list
        graph = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            graph[prereq].append(course)

        # 2. Track node states
        visiting = set()
        visited = set()

        def dfs(node):
            # 3. Encountered a node on current path
            if node in visiting:
                return False

            # 4. Already fully explored
            if node in visited:
                return True

            # 5. Start exploring this node
            visiting.add(node)

            # 6. Recursively explore neighbors
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

            # 7. All neighbors checked successfully
            visiting.remove(node)
            visited.add(node)

            return True

        # 8. Check every node, including disconnected ones
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True

