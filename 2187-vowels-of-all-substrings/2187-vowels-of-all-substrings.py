class Solution:
    def countVowels(self, word: str) -> int:
        vowels={'a','e','i','o','u'}
        answer=0
        n=len(word)
        for i ,ch in enumerate(word):
            if ch in vowels:
                answer+=(i+1)*(n-i)
        return answer
        