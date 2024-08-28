class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        unique_nums = set(nums)
        largest = 0

        for x in unique_nums:
            # Only start counting if x is the start of a sequence
            if x - 1 not in unique_nums:
                count = 1
                current_num = x
                
                while current_num + 1 in unique_nums:
                    current_num += 1
                    count += 1
                
                largest = max(largest, count)
        
        return largest

