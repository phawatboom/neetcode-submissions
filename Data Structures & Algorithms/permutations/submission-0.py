class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = [False for _ in range(len(nums))]
        perm = []

        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for i in range(len(nums)):
                if temp[i] == True:
                    continue
                temp[i] = True
                perm.append(nums[i])
                dfs()

                temp[i] = False
                perm.pop()
        
        dfs()
        return res

            