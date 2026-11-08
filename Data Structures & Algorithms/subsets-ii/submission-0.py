class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
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
        # for e in res:
        #     if 
        res = [sorted(e) for e in res]
        return list(set(tuple(e) for e in res))


# class Solution:
#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
#         res = []
#         subset = []

#         def dfs(i, dup):
#             if i == len(nums):
#                 res.append(subset.copy())
#                 return 

#             if nums[i] not in subset:
#                 subset.append(nums[i])
#                 dup = False
            
#             dfs(i + 1, dup)
            
#             if dup == True:
#                 subset.pop()
#             dfs(i + 1, dup)
    
#         dfs(0, True)
#         return res set()