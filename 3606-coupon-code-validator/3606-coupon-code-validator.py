class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        valid_lines = ["electronics", "grocery", "pharmacy", "restaurant"]

        def is_valid_code(c: str) -> bool:
            return c != "" and all(ch.isalnum() or ch == "_" for ch in c)

        valid = []
        for c, bl, active in zip(code, businessLine, isActive):
            if active and bl in valid_lines and is_valid_code(c):
                valid.append((bl, c))

        valid.sort(key=lambda x: (valid_lines.index(x[0]), x[1]))

        return [c for _, c in valid]
        