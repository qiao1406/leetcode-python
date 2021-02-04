import heapq


class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """

        if len(buildings) == 0:
            return []

        b = []
        for x1, x2, y in buildings:
            b.append((x1, -y))
            b.append((x2, y))
        b.sort()

        res = []
        pq = []
        heapq.heappush(pq, 0)
        pre_max = 0

        for x, y in b:
            if y < 0:
                heapq.heappush(pq, y)
            else:
                pq.remove(-y)
                heapq.heapify(pq)
            pq_max = 0 - pq[0]

            if pre_max != pq_max:
                res.append([x, pq_max])
                pre_max = pq_max

        return res


s = Solution()
print(s.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
