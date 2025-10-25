class Solution:
    def totalMoney(self, n: int) -> int:
        
        ans = 0
        days = 0
        curr_monday = 0
        week_day = 0

        i = 0
        while(days < n):

            if(week_day == 0):
                curr_monday += 1
            
            ans += curr_monday + week_day

            week_day = (week_day + 1) % 7
            days += 1    

        return ans