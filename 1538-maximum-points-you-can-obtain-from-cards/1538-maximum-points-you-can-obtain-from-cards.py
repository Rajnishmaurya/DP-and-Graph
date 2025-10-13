class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k==len(cardPoints):
            return sum(cardPoints)
        
        total=sum(cardPoints[:k])
        result=total

        end=len(cardPoints)-1

        while k>0:
            total-=cardPoints[k-1]
            total+=cardPoints[end]
            result=max(result,total)
            end-=1
            k-=1
        return result
        