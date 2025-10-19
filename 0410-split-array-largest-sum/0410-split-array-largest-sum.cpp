#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    bool solve(vector<int>&nums,int mid,int k)
    {
        int total=0;
        int n=nums.size();
        int pieces=1;
        for(int i=0;i<n;i++)
        {
            if (total+nums[i]<=mid)
            {
                total=total+nums[i];
            }
            else
            {
                total=nums[i];
                pieces+=1;
                if (pieces>k)
                {
                    return false;
                }
            }
        }
        return true;
    }
    int splitArray(vector<int>& nums, int k) {
        int left=0;
        int right=0;
        int n=nums.size();

        for(int i=0;i<n;i++)
        {
            left=max(left,nums[i]);
            right+=nums[i];
        }

        while (left<=right)
        {
            int mid=(left+right)/2;
            if(solve(nums,mid,k))
            {
                right=mid-1;
            }
            else
            {
                left=mid+1;
            }
        }
        return left;
        
    }
};