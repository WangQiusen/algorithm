class Solution(object)
    def canCross(self, stones)
        """
        :type stones: List[int]
        :rtype: bool
        """
        n = len(stones)
        pos = set(stones)
        seen = set()
        @lru_cache(None)
        def dfs(cur, k):
            if cur == stones[n - 1]:
                return True
            if not cur in pos:
                return False
            if (cur, k) in seen:
                return False
            seen.add((cur, k))
            return dfs(cur + k - 1, k - 1) or dfs(cur + k, k) or dfs(cur + k + 1, k + 1)
        return dfs(stones[0] + 1, 1)