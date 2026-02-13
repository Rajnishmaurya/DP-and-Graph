class Solution:
    def longestBalanced(self, s: str) -> int:
        f, m, r = [0, 0, 0], {(i, 0, 0): 0 for i in range(4)}, max(sum(1 for _ in g) for _, g in groupby(s))
        for i, c in enumerate(s, 1):
            f[ord(c) - ord('a')] += 1
            r = max(r, i - m.setdefault((0, f[0]-f[1], f[1]-f[2]), i))
            r = max(r, i - m.setdefault((1, f[0]-f[1], f[2]), i))
            r = max(r, i - m.setdefault((2, f[1]-f[2], f[0]), i))
            r = max(r, i - m.setdefault((3, f[2]-f[0], f[1]), i))
        return r