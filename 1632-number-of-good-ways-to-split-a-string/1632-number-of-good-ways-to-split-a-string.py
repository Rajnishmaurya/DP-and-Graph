class Solution:
    def numSplits(self, s: str) -> int:
        count=0
        right=Counter(s)
        left=Counter()

        for ch in s:
            right[ch]-=1
            left[ch]+=1

            if right[ch]==0:
                del right[ch]
            
            if len(left)==len(right):
                count+=1
        return count
        # count=0
        # n=len(s)

        # for i in range(n):
        #     d1=Counter(s[0:i+1])
        #     d2=Counter(s[i+1:n])
        #     if len(d1)==len(d2):
        #         count+=1
        # return count
        