class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        diffs = {}
        for i in range(len(nums)):
            d = target - nums[i]
            if d in diffs:
                return [diffs[d], i]
            else:
                diffs[nums[i]] = i
        

        