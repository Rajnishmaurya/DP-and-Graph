class Solution:
    def maxFreqSum(self, s: str) -> int:
        hashmap = {}
        vowel = 0
        consonant = 0

        for ch in s:
            if ch not in hashmap:
                hashmap[ch] = 0
            hashmap[ch] += 1
            if ch in "aeiou":
                vowel = max(hashmap[ch], vowel)
            else:
                consonant = max(hashmap[ch], consonant)
        return consonant + vowel