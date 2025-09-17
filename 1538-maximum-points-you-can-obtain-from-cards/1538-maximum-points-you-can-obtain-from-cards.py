class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        temp=sum(cardPoints[:k])

        n=len(cardPoints)
        end=n-1
        result=temp
        while k>0:
            temp-=cardPoints[k-1]
            temp+=cardPoints[end]
            result=max(result,temp)
            k-=1
            end-=1
        return result