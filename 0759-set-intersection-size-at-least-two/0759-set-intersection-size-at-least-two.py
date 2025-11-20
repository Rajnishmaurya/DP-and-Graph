class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        
        min_set_size = 0
        # Track the 2 largest numbers chosen so far
        second_largest = float("-inf")
        largest = float("-inf")
        
        for start, end in intervals:
            # Case 1: Current interval has fewer than 2 of our chosen numbers
            # We need to add new numbers to cover this interval
            if start > largest:
                min_set_size += 2
                second_largest = end - 1
                largest = end
            # Case 2: Current interval has exactly 1 of our chosen numbers  
            # We need to add 1 more number
            elif start > second_largest:
                min_set_size += 1
                second_largest = largest
                largest = end
        
        return min_set_size