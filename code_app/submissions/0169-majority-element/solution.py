class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        half = len(nums)//2
        tracker = {}
        for i in range(len(nums)):
            tracker[nums[i]] = tracker.get(nums[i], 0) +1
            if tracker[nums[i]] > half:
                return nums[i]
