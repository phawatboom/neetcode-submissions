class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix_sum = [1] * len(nums)
        total = 1
        for i in range(1, len(nums)):
            total *= nums[i - 1]
            prefix_sum[i] = total
            prefix_sum.append(total)
        
        suffix = [1] * len(nums)
        # print(prefix_sum)
        total = 1
        for i in range(len(nums) -2, -1, -1):
            total *= nums[i + 1]
            suffix[i] = total
            
        # print(suffix)
        for i in range(len(nums)):
            # print(prefix_sum[i])
            # print(suffix[i])
            res.append(prefix_sum[i] * suffix[i])

        return res