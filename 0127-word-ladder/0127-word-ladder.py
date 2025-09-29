class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordlist=set(wordList)

        if endWord not in wordlist:
            return 0
        
        q=deque()
        q.append((beginWord,1))
        
        while q:
            word,step=q.popleft()

            for i in range(len(word)):
                for j in range(26):
                    new_word=word[:i]+chr(97+j)+word[i+1:]
                    if new_word==endWord:
                        return step+1
                    if new_word in wordlist:
                        q.append((new_word,step+1))
                        wordlist.remove(new_word)
        
        return 0

            

        