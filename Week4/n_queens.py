class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def search(can,n,i):
            if i == n: return [transfer(can,n)]
            else:
                res = []
                for j in range(n):
                    if check(can, i, j):
                        can[i]=j
                        res.extend(search(can,n,i+1))
                return res

        def check(can,i,j):
            return all(j != v and i+j!=k+v and i-k!=j-v for k,v in enumerate(can[:i]))

        def transfer(can,n):
            return ["."*v+"Q"+"."*(n-v-1) for v in can]
        
        return search([0]*n,n,0)