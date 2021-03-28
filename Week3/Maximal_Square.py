class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        r = len(matrix)
        c = len(matrix[0])
        longest = 0
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == '1':
                    if longest == 0:
                        longest = 1
                    if i-1 < 0 or j-1 < 0:
                        continue
                    matrix[i][j] = 1 + min(int(matrix[i-1][j-1]), int(matrix[i][j-1]), int(matrix[i-1][j]))
                    longest = max(longest, matrix[i][j])
        return longest ** 2