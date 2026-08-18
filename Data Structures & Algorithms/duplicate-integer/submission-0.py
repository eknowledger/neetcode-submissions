class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        numsCount = set()
        for i in nums:
            if i in numsCount:
                return True
            else:
                numsCount.add(i)

        return False
        