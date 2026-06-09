class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = dict()
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
        for key in freq:
            if freq[key] > n//2:
                return key
        