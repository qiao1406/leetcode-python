class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        res = ['()']

        for i in range(1, n):
            s = set()
            for r in res:
                for j in range(1, len(r) + 1):
                    tmp = r[:j] + '()' + r[j:]
                    s.add(tmp)

            res = list(s)

        return res


s = Solution()
print(s.generateParenthesis(3))
