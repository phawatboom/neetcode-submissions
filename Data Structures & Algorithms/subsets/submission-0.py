class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        subset = []
        def dfs(level):
            if level == len(nums):
                res.append(subset.copy())
                return 
            
            #include
            subset.append(nums[level])
            dfs(level + 1)

            # exclude
            subset.pop()
            dfs(level + 1)
            
        dfs(0)
        return res
