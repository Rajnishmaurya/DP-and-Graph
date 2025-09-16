class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        

        hand.sort()

        count=Counter(hand)

        for num in hand:
            if count[num]==0:
                continue
            for i in range(groupSize):
                if count[num+i]>0:
                    count[num+i]-=1
                else:
                    return False
        return True