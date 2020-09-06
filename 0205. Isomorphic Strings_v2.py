class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        size_s = len(s)
        size_t = len(t)
        temp_dict = {}

        # check the length of the string
        if size_s != size_t:
            return False

        # put the same index of the string into the temp_dict
        for i in range(size_s):
            # if s[i] and t[i] are both not in the temp_dict, create it
            if s[i] not in temp_dict:
                if t[i] not in temp_dict.values():
                    temp_dict[s[i]] = t[i]
                else:
                    # if t[i] is in the temp_dict.values(), return False
                    return False
            # if s[i] is in the temp_dict, and check the values of temp_dict[s[i]]
            if temp_dict[s[i]] != t[i]:
                return False
        # finish checking and return True
        return True


sol = Solution()
s = "aab"
t = "aba"
print(sol.isIsomorphic(s, t))
