class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_table = {}
        for i in range(len(nums)):
            if nums[i] in hash_table:
                return True
            else:
                hash_table[nums[i]] = True
        return False