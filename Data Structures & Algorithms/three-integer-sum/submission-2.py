class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        nums.sort()
        for j in range(len(nums)):
            seen = set()
            for k in range(j + 1, len(nums)):
                complement = - nums[j] - nums[k]
                if complement in seen:
                    triplet = tuple(sorted([complement, nums[j], nums[k]]))
                    if triplet not in res:
                        res.append(triplet)
                seen.add(nums[k])
        
        return res            
