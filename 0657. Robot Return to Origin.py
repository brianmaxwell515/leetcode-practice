class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        if(moves.count("L") == moves.count("R")) and (moves.count("U") == moves.count("D")):
            return True
        else:
            return False


sol = Solution()
moves = "LLRR"
print(sol.judgeCircle(moves))
