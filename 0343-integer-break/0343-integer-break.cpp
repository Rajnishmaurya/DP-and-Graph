class Solution {
public:
    int integerBreak(int n) {
        if (n == 2)
            return 1;
        if (n == 3)
            return 2;

        vector<int> dp(n + 1, 0);
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 3;

        for (int num = 4; num <= n; num++) {
            int maxi = 0;
            for (int i = 1; i <= num / 2; i++) {
                maxi = max(maxi, dp[i] * dp[num - i]);
            }
            dp[num] = maxi;
        }

        return dp[n];
    }
};
