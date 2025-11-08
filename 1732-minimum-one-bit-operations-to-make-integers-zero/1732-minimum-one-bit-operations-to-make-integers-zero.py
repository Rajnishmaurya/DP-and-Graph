class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        s = bin(n)[2:]

        bit = s[0]

        for i in range(1, len(s)):
            if bit[i - 1] == s[i]:
                bit += "0"
            else:
                bit += "1"

        return int(bit, 2)