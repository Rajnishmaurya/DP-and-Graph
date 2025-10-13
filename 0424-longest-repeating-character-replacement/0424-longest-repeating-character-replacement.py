class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        lis=[0]*26
        max_len=0
        max_freq=0

        for right in range(len(s)):
            temp=ord(s[right])-ord('A')
            lis[temp]+=1

            max_freq=max(max_freq,lis[temp])

            if right-left+1-max_freq>k:
                index=ord(s[left])-ord('A')
                lis[index]-=1
                left+=1
            max_len=max(max_len,right-left+1)
        return max_len        