from datetime import datetime


class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        return datetime(year, month, day).strftime('%A')


sol = Solution()
day, month, year = 31, 8, 2019
print(sol.dayOfTheWeek(day, month, year))
