class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        temp=0
        count=0
        for num in target:
            if num>temp:
                count+=num-temp
            temp=num
        return count
        