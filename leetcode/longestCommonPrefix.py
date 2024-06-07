class Solution:
    def longestCommonPrefix(self, strs) -> str:
        longest = ""
        go_on = True

        for j in range(len(strs[0])):  # Letter in First Word
            for k in range(len(strs)):  # All other Words
                if strs[0][: j + 1] != strs[k][: j + 1]:
                    go_on = False
                    break
                if k == len(strs) - 1:  # Last Word
                    longest = strs[0][: j + 1]
            if not go_on:
                break

        return longest


sol = Solution()

sol.longestCommonPrefix(["flower", "flow", "flight", "flowed"])
sol.longestCommonPrefix(["dog", "racecar", "car"])
sol.longestCommonPrefix(["a"])
print(
    sol.longestCommonPrefix(["flower", "flower", "flower", "flower"])
)  # Expected: "fl"
