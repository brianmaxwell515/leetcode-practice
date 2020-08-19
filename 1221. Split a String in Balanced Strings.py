class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        l_count, r_count, res = 0, 0, 0
        for i in s:
            if i == "L":
                l_count += 1
            else:
                r_count += 1
            if l_count == r_count:
                res += 1
                l_count = r_count = 0
        return res


sol = Solution()
s = "RLRRLLRLRL"
print(sol.balancedStringSplit(s))
