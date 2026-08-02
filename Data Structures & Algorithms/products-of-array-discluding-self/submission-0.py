class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1] * len(nums)
        
        left_products = [1] * len(nums)
        left_running_product = 1
        for i in range(len(nums)):
            left_products[i] = left_running_product
            left_running_product *= nums[i]

        right_products = [1] * len(nums)
        right_running_product = 1
        for i in reversed(range(len(nums))):
            right_products[i] = right_running_product
            right_running_product *= nums[i]

        for i in range(len(nums)):
            products[i] = left_products[i] * right_products[i]

        return products