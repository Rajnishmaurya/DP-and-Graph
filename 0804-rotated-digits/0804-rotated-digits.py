class Solution:
    def rotatedDigits(self, n: int) -> int:
        count=0
        for i in range(1,n+1):
            digit=str(i)
            if '3' in digit or '4' in digit or '7' in digit:
                continue
            if '2' in digit or '5' in digit or '6' in digit or '9' in digit:
                count+=1
        return count
        