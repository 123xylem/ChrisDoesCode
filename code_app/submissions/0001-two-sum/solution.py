class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # tried sorting array - using mid point as start of search
        # mid_point = int(round(len(nums_sorted)/2,0))
        #iterate through arr with 1 fixed point
        #if no match at end of length move fixed point
        index = 0
        while True:
            for i in range(index, len(nums) -1):
                if nums[index] + nums[i+1] == target:
                    return [index, i+1]
            else:
                index += 1
                for i in range(index, len(nums) -1 ):
                    if nums[index] + nums[i+1] == target:
                        return [index, i+1]

            
