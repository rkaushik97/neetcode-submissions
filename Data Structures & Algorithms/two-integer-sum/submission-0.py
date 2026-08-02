class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in lookup:
                return [lookup[difference], i]
            else:
                lookup[num] = i
        return []