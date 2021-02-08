class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if len(nums) == 0:
            return [-1, -1]

        l, r = 0, len(nums) - 1
        mid = 0

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                break
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        if l > r:
            return [-1, -1]
        mid_l = mid_r = mid

        if nums[l] == target:
            mid_l = l
            l = 0
        while l < mid_l:
            s = (l + mid_l) // 2
            if nums[s] == target:
                if s == 0:
                    l = 0
                    break
                else:
                    if nums[s - 1] != target:
                        l = s
                        break
                    else:
                        mid_l = s - 1
            else:
                l = s + 1

        if nums[r] == target:
            mid_r = r
            r = len(nums) - 1
        while r > mid_r:
            e = (r + mid_r) // 2
            if nums[e] == target:
                if e == len(nums) - 1:
                    r = e
                    break
                else:
                    if nums[e + 1] != target:
                        r = e
                        break
                    else:
                        mid_r = e + 1
            else:
                r = e - 1
        return [l, r]


s = Solution()
print(s.searchRange([5, 7, 7, 8, 8, 10], 8))
print(s.searchRange([5, 5, 5, 5, 5], 5))
print(s.searchRange([5, 6, 7], 6))
