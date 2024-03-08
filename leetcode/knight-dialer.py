# Max recursion depth

class Solution(object):
    def knightDialer(self, n):
        self.valid_jumps = [
            [4, 6],
            [6, 8],
            [7, 9],
            [4, 8],
            [0, 3, 9],
            [],
            [0, 1, 7],
            [2, 6],
            [1, 3],
            [2, 4],
            [4, 6],
        ]

        self.retur = 0
        for i in self.valid_jumps:
            for j in i:
                self.recursive(n, j, 1)

        return self.retur % 10

    def recursive(self, n, tall, teller):
        teller += 1
        if teller == n:
            self.retur += 1
        else:
            for i in self.valid_jumps[tall]:
                self.recursive(n, i, teller)
