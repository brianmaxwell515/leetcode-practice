class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace('.','[.]')

sol = Solution()
address = "1.1.1.1"
print(sol.defangIPaddr(address))