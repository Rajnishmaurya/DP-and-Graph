class Solution:
    def solve(self,result,temp,open,close):
        if open==0 and close==0:
            result.append(temp)
            return 
        if open:
            self.solve(result,temp+"(",open-1,close)
        if close>open:
            self.solve(result,temp+")",open,close-1)
            
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        temp=""
        self.solve(result,temp,n,n)
        return result
        