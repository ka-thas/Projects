class Solution(object):
    def romanToInt(self, s):
        dict = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }

        return_integer = 0
        for i in range(len(s)):
            if i < len(s)-1 and dict[s[i]] < dict[s[i+1]]:
                return_integer -= dict[s[i]]
            else:
                return_integer += dict[s[i]]
        return return_integer