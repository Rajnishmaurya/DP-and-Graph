class Solution:
    # def is_palindrome(self,s):
    #     start,end=0,len(s)-1
    #     while start<end:
    #         if s[start]!=s[end]:
    #             return False
    #         start+=1
    #         end-=1
    #     return True
    def longestPalindrome(self, s: str) -> str:
        if len(s)<=1:
            return s
        
        max_len=1
        ans=s[0]

        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if j-i+1>max_len and s[i:j+1]==s[i:j+1][::-1]:
                    max_len=j-i+1
                    ans=s[i:j+1]
        return ans