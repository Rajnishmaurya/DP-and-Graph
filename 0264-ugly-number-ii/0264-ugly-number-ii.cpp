class Solution {
public:
    int nthUglyNumber(int n) {
        vector<int>ans(n);
        ans[0]=1;
        int i2=0,i3=0,i5=0;
        for(int i=1;i<n;i++)
        {
            int next2 = ans[i2] * 2;
            int next3 = ans[i3] * 3;
            int next5 = ans[i5] * 5;
            int next_n=min(next2,min(next3,next5));
            ans[i]=next_n;
            if(next_n==next2)
            i2+=1;

            if(next_n==next3) i3+=1;
            if(next_n==next5) i5+=1;
        }
        return ans[n-1];

        
    }
};