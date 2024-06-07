class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        index_ptr = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            else:
                nums[index_ptr] = nums[i]
                index_ptr += 1

        return index_ptr

    def test(self):
        nums = [1, 1, 2, 3]
        # Input array
        expectedNums = [1, 2, 3, 3]
        # The expected answer with correct length

        k = self.removeDuplicates(nums)
        print(k)
        # Calls your implementation

        print(k == len(expectedNums))

        for i in range(k):
            assert nums[i] == expectedNums[i]


s = Solution()
s.test()
