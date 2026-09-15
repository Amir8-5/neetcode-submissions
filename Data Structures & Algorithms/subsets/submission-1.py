class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        sub = []

        def back(i) :
            if i == len(nums):
                temp = sub.copy()
                if temp not in res:
                    res.append(temp)
                return
            
            sub.append(nums[i])
            back(i+1)
            sub.pop()
            back(i+1)
            return

        

        back(0)
        return res