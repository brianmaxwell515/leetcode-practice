class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        temp_i = {}
        temp_j = {}
        list_i = []
        list_j = []

        # {'p': 0, 'a': 1, 'e': 3, 'r': 4}
        for i in range(len(s)):
            if s[i] in temp_i.keys():
                continue
            else:
                temp_i[s[i]] = i

        # [0, 1, 0, 3, 4]
        for i in s:
            list_i.append(temp_i[i])

        # {'t': 0, 'i': 1, 'l': 3, 'e': 4}
        for j in range(len(t)):
            if t[j] in temp_j.keys():
                continue
            else:
                temp_j[t[j]] = j

        # [0, 1, 0, 3, 4]
        for j in t:
            list_j.append(temp_j[j])

        # print(temp_i)
        # print(temp_j)
        # print(temp_i.values())
        # print(temp_j.values())
        # print(list_i)
        # print(list_j)

        if list_i == list_j:
            return True
        else:
            return False


sol = Solution()
s = "paper"
t = "title"
print(sol.isIsomorphic(s, t))
