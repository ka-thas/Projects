class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        return x[::-1] == x