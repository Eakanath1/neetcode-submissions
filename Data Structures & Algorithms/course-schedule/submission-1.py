class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        adj_list = [[] for _ in range(numCourses)]
        for (cur, pre) in prerequisites:
            indegree[cur] += 1
            adj_list[pre].append(cur)
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        can_take = 0
        while q:
            cur = q.popleft()
            can_take += 1
            for course in adj_list[cur]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    q.append(course)
        return can_take == numCourses