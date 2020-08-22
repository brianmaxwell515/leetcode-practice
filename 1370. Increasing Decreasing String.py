class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        s = list(s)
        while(len(s) > 0):
            templist = s
            templist = sorted(list(set(templist)))
            for i in templist:
                res.append(i)
                s.remove(i)

            templist = s
            templist = sorted(list(set(templist)), reverse=True)
            for i in templist:
                res.append(i)
                s.remove(i)
        return "".join(res)


sol = Solution()
s = "aaaabbbbcccc"
print(sol.sortString(s))
