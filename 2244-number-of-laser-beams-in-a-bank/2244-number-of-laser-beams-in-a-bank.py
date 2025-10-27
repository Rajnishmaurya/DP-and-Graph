class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        if not bank:
            return 0

        sd = [0] * len(bank)
        row = 0

        for it in bank:
            count = 0
            for i in range(len(bank[0])):
                if it[i] == '1':
                    count += 1
            sd[row] = count
            row += 1

        sdwz = [x for x in sd if x != 0]
        ans = 0

        if len(sdwz) <= 1:
            return ans

        for i in range(len(sdwz) - 1):
            ans += sdwz[i] * sdwz[i + 1]

        return ans