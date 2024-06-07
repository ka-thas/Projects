class Solution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        i = 0
        j = 1
        fractions = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                fractions.append([arr[i], arr[j]])

        # Sort the fractions by value, but keep the numbers
        fractions = self.quickSortFractions(fractions)
        return fractions[k - 1]

    def quickSortFractions(self, fractions):
        if len(fractions) <= 1:
            return fractions
        pivot = fractions[0]
        left = []
        right = []
        for i in range(1, len(fractions)):
            pivot_value = pivot[0] / pivot[1]
            i_value = fractions[i][0] / fractions[i][1]
            if i_value < pivot_value:
                left.append(fractions[i])
            else:
                right.append(fractions[i])
        return self.quickSortFractions(left) + [pivot] + self.quickSortFractions(right)

    def quickSort(self, list):
        if len(list) <= 1:
            return list
        pivot = list[0]
        left = []
        right = []
        for i in range(1, len(list)):
            if list[i] < pivot:
                left.append(list[i])
            else:
                right.append(list[i])
        return quickSort(left) + [pivot] + quickSort(right)

    def test(self):
        # result = self.kthSmallestPrimeFraction([1, 7], 1)
        result = self.kthSmallestPrimeFraction([1, 2, 3, 5], 3)
        print(result)


s = Solution()
s.test()
