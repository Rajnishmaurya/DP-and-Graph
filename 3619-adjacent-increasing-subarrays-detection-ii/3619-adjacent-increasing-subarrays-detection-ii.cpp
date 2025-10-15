class Solution {
public:
    int maxIncreasingSubarrays(vector<int>& nums) {
        int ans=1,count=1,prev=0,n=nums.size();

        for(int i=1;i<n;i++)
        {
            if (nums[i]>nums[i-1])
            {
                count++;
            }
            else
            {
                prev=count;
                count=1;
            }
            ans=max(ans,min(prev,count));
            ans=max(ans,count/2);
        }
        return ans;
    }
};