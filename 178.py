class Num(object):

    def __init__(self, number):
        self.number = str(number)
        self.ori_num = number

    def __len__(self):
        return len(self.number)

    def __repr__(self):
        return self.number

    def __eq__(self, other):
        return self.number == other.number

    def __gt__(self, other):
        if len(self) == len(other):
            return self.ori_num > other.ori_num

        if len(self) < len(other):
            return not other.__gt__(self)

        i = 0
        while i < len(other) and self.number[i] == other.number[i]:
            i += 1
        if i == len(other):
            if self.number[i] == '0':
                return False
            new_num = Num(int(self.number[i:]))
            return new_num.__gt__(other)
        else:
            return int(self.number[i]) > int(other.number[i])


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        l = [Num(num) for num in nums]
        l = sorted(l, reverse=True)
        s = ''.join([num.number for num in l])
        return '0' if s[0] == '0' else s


s = Solution()
print(s.largestNumber([3, 30, 34, 5, 9]))
# print(s.largestNumber([432, 43243243]))
