class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
         
        # get product of all values on left (minus moving i )
        # get prod of all on right (minus i)
        # times these 2 array vals together to get a product that has minused i
        # return result
        res = []
        left_arr = [1] * len(nums)
        right_arr = [1] * len(nums)
        for i in range(1, len(nums)):
            left_arr[i] *= nums[i-1] * left_arr[i-1]
        for i in range(len(nums) -2, -1, -1):
            right_arr[i] *= nums[i+1] * right_arr[i+1]

        for x in range(len(right_arr)):
            res.append(right_arr[x] * left_arr[x])
        return res
