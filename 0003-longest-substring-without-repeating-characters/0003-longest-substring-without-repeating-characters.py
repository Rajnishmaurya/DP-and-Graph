class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st=set()
        result=0
        l=0
        for r in range(len(s)):
            if s[r] in st:
                while l<r and s[r] in st:
                    st.remove(s[l])
                    l+=1
            st.add(s[r])
            result=max(result,r-l+1)
        return result

        