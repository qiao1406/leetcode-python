from functools import reduce


class Solution(object):

    def dfs(self, start, y):
        for end in self.m[start]:

            if end in self.s:
                continue

            self.s.append(end)
            self.v.append(self.m[start][end])
            if end == y:
                self.v2 = self.v[:]
                self.s2 = self.s[:]
                return
            else:
                self.dfs(end, y)
                self.s.pop()
                self.v.pop()

    def seek(self, x, y):
        self.s = [x]
        self.v = [1]
        self.s2 = []
        self.v2 = []

        self.dfs(x, y)

        if not self.s2:
            return -1
        else:
            print(self.v2)
            val = reduce(lambda a, b: a * b, self.v2)
            return 1 / val

    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """

        m = {}
        for i in range(len(equations)):
            a, b = equations[i]
            v = values[i]

            if a not in m:
                m[a] = {}
            if b not in m:
                m[b] = {}

            m[a][b] = 1 / v
            m[b][a] = v

        self.m = m

        ans = []
        for a, b in queries:
            if a not in self.m or b not in self.m:
                ans.append(-1)
                continue
            if a == b:
                ans.append(1)
            elif a in self.m[b]:
                ans.append(self.m[b][a])
            else:
                ans.append(self.seek(a, b))

        return ans

s = Solution()
res = s.calcEquation([["p","q"],["m","n"],["q","n"]], [2.0,3.0,2], [["p","m"]])
print(res)
