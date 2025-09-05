class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack=[float('inf')]
        result=0

        for num in arr:
            while stack and stack[-1]<=num:
                current=stack.pop()
                if stack:
                    result+=current*min(stack[-1],num)
            stack.append(num)
        while len(stack)>2:
            result+=stack.pop()*stack[-1]
        return result
        