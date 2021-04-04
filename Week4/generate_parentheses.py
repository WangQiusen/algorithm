class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
                result=[]
        left,right=0,0
        def generateResult(str,n,left,right):
            if left>n or left<right:
                return
            if len(str)==2*n:
                result.append(str)
                return
            generateResult(str+'(',n,left+1,right)
            generateResult(str+')',n,left,right+1)
        generateResult("",n,0,0)
        return result