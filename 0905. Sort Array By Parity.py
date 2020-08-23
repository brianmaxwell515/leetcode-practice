class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = []
        for i in A:
            if i % 2 == 0:
                res.insert(0, i)
            else:
                res.append(i)
        return res


A = [3, 1, 2, 4]
print(Solution.sortArrayByParity(1, A))
