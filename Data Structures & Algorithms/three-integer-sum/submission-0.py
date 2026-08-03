class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for idx in range(len(nums)):
            left_idx = idx+1
            right_idx = len(nums)-1

            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
            
            while left_idx < right_idx:
                addition = nums[idx] + nums[left_idx] + nums[right_idx]
                
                if addition == 0:
                    result.append([nums[idx], nums[left_idx], nums[right_idx]])
                    left_idx += 1
                    right_idx -= 1
                    while left_idx < right_idx and nums[left_idx] == nums[left_idx - 1]:
                        left_idx += 1

                if addition < 0:
                    left_idx += 1

                if addition > 0:
                    right_idx -= 1
                    
        return result