#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int maxRotateFunction(vector<int>& nums) {
        int total=0;
        int n=nums.size();
        int temp=0;
        for(int i=0;i<n;i++)
        {
            total+=i*nums[i];
            temp+=nums[i];
        }
        vector<int>dp(n,0);
        dp[0]=total;
        int maxi=dp[0];

        for(int i=1;i<n;i++)
        {
            dp[i]=dp[i-1]+temp-n*nums[n-i];
            maxi=max(maxi,dp[i]);
        }
        return maxi;



        
    }
};