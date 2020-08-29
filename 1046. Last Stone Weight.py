class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while len(stones) > 1:
            m = max(stones)
            stones.remove(m)
            n = max(stones)
            stones.remove(n)
            stones.append(abs(m-n))
        return stones[0]


sol = Solution()
stones = [1, 3]
# stones = [2, 7, 4, 1, 8, 1]
print(sol.lastStoneWeight(stones))
