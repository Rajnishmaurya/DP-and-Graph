class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lis=[0]*26
        l=0
        r=0
        max_len=0
        max_freq=0

        for r in range(len(s)):
            temp=ord(s[r])-ord('A')
            lis[temp]+=1
            max_freq=max(max_freq,lis[temp])
            if r-l+1-max_freq>k:
                index=ord(s[l])-ord('A')
                lis[index]-=1
                l+=1

            max_len=max(max_len,r-l+1)
        return max_len

            
        