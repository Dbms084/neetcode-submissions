class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap = {}
        for i,val in enumerate(nums):
            diff = target - val
            if diff in prevmap:
                return [prevmap[diff],i]
            prevmap[val] = i
        