class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        count=Counter(power)
        power_count=[]
        for p in sorted(count.keys()):
            power_count.append((p,count[p]))

        cache={}

        def solve(index):
            if index in cache:
                return cache[index]

            if index>=len(power_count):
                return 0
            
            not_taken=solve(index+1)

            power,count=power_count[index]
            
            next_index=bisect.bisect_left(power_count,(power+3,-1))

            taken=power*count+solve(next_index)

            cache[index]=max(taken,not_taken)
            return cache[index]
        
        return solve(0)
        