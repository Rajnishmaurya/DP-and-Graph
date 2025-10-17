class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        
        int ans=0;
        int result=INT_MIN;

        int n=nums.size();

        for(int i=0;i<n;i++)
        {
            ans+=nums[i];
            result=max(result,ans);

            if (ans<0)
            {
                ans=0;
            }
            
        }
        return result;
    }
};