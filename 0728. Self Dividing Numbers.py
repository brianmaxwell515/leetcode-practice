class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for i in range(left, right):
            uninum = str(i)
            count = 0
            for j in uninum:
                if j == '0':
                    count += 1
                    break
                elif i % int(j) != 0:
                    count += 1
                    break
            if count == 0:
                res.append(i)
        return res


sol = Solution()
left = 1
right = 22
print(sol.selfDividingNumbers(left, right))
