class Solution(object):
    def sortArrayByParity(self, A):
        A.sort(key=lambda x: x % 2)
        return A


sol = Solution()
A = [3, 1, 2, 4]
print(sol.sortArrayByParity(A))
