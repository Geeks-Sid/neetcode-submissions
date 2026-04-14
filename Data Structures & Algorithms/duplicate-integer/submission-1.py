class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp = {}
        for i in nums:
            print(i not in temp)
            if i not in temp:
                temp[i] = 1
            else:
                return True
        return False