class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        result=0

        q=deque(initialBoxes)
        visit=set()

        while q:
            current_box=q.popleft()
            if current_box in visit:
                continue
            visit.add(current_box)

            if status[current_box]:
                result+=candies[current_box]

                for k in keys[current_box]:
                    if k in visit and status[k]==0:
                        status[k]=1
                        q.append(k)
                        visit.remove(k)
                    else:
                        status[k]=1

                for box in containedBoxes[current_box]:
                    q.append(box)
        return result
        