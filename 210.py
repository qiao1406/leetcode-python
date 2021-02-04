class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        graph = {}
        visited = [0] * numCourses

        for i, j in prerequisites:
            if i not in graph:
                graph[i] = set()
            graph[i].add(j)

        seq = [i for i in range(numCourses) if i not in graph]

        def dfs(node):
            # print(node)
            f = True
            if node not in graph:
                visited[node] = 2
                # seq.append(node)
                return True

            visited[node] = 1
            for son in graph[node]:

                if visited[son] == 2:
                    continue

                if visited[son] == 1:
                    return False
                else:
                    f = f and dfs(son)

            visited[node] = 2
            seq.append(node)
            return f

        flag = True
        for i in graph:
            if visited[i] == 0:
                flag = flag and dfs(i)

        return seq if flag else []


s = Solution()
# print(s.findOrder(2, [[1, 0], [0, 1]]))
print(s.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
