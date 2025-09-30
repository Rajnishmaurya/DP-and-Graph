class Solution:
    def solve(self,index,amount,coins,dp):
        if index==0:
            if amount%coins[index]==0:
                return amount//coins[index]
            return int(1e9)
        
        if dp[index][amount]!=-1:
            return dp[index][amount]
        
        not_taken=self.solve(index-1,amount,coins,dp)
        taken=int(1e9)
        if coins[index]<=amount:
            taken=1+self.solve(index,amount-coins[index],coins,dp)
        
        dp[index][amount]=min(not_taken,taken)
        return dp[index][amount]
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)

        dp=[[-1 for _ in range(amount+1)] for _ in range(n)]

        ans=self.solve(n-1,amount,coins,dp)
        if ans==int(1e9):
            return -1
        else:
            return ans