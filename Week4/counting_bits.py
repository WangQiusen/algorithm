class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        bits = [0]
        for i in range(1, num + 1):
            bits.append(bits[i & (i - 1)] + 1)
        return bits