class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dicts={}
        for values,key in enumerate(nums):
            dicts[key]=values
        return min(dicts.keys())