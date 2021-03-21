class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)/2]

if __name__ == "__main__":
    lists = [2,2,1,1,2,2]
    target = Solution()
    print("the most one is {}".format(target.majorityElement(lists)))