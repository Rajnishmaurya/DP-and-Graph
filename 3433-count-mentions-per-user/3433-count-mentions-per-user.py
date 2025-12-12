class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        dp = [0] * numberOfUsers
        onl = [0] * numberOfUsers
        events.sort(key = lambda x : (int(x[1]), x[0] == "MESSAGE"))
        for msg, time, ppl in events:
            t = int(time)
            if msg == "MESSAGE":
                if ppl == "ALL":
                    for i in range(numberOfUsers):
                        dp[i] += 1
                elif ppl == "HERE":
                    for i in range(numberOfUsers):
                        if t >= onl[i]:
                            dp[i] += 1
                else:
                    for p in ppl.replace("id", "").split():
                        dp[int(p)] += 1
            else:
                onl[int(ppl)] = t + 60
        return dp
