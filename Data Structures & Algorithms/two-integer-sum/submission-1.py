class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in hash_table:
                return [hash_table[compliment], i]
            else:
                hash_table[nums[i]] = i
            