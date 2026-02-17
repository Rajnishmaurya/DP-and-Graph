class Solution:
    def readBinaryWatch(self, n: int) -> List[str]:
        return [f'{h}:{m:02d}' for q in combinations((1j,2j,4j,8j,1,2,4,8,16,32),n)
            if (h:=int(sum(q).imag))<12 and (m:=int(sum(q).real))<60]