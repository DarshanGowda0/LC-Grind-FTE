class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # topological sort
        
        indegree = {i: 0 for i in range(numCourses)}
        adjList = {i: [] for i in range(numCourses)}
        
        for c in prerequisites:
            dest, source = c
            adjList[source] += dest,
            indegree[dest] += 1
        
        que = deque()
        
        for idx, i in indegree.items():
            if i == 0:
                que += idx,
              
        res = []
        while que:
            course = que.popleft()
            res += course,
            for child in adjList[course]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    que += child,
                    
        return len(res) == numCourses