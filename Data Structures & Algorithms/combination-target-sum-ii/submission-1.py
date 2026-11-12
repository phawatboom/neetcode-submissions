class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        combination = []
        candidates.sort()
        
        def dfs(start, total):
            if total > target:
                return
            if total == target:
                res.append(sorted(combination[:]))
                return 
            
            for i in range(start, len(candidates)):

                if total + candidates[i] > target:
                    break
                
                if i > start and candidates[i - 1] == candidates[i]:
                    continue

                combination.append(candidates[i])
                dfs(i + 1, total + candidates[i])
                combination.pop()
        dfs(0, 0)
        return res