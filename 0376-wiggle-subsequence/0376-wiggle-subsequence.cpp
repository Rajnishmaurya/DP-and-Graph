#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        int up=1,down=1;

        int n=nums.size();
        for(int i=1;i<n;i++)
        {
            if(nums[i]>nums[i-1])
            {
                up=down+1;
            }
            if(nums[i]<nums[i-1])
            {
                down=up+1;
            }
        }
        return max(up,down);
        
    }
};