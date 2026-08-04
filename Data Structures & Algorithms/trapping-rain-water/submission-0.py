class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = len(height) * [0]
        for i in range(len(height)):
            if i == 0:
                max_left[i] = height[i]
                continue
            max_left[i] = max(max_left[i-1], height[i])

        max_right = len(height) * [0]
        for i in reversed(range(len(height))):
            if i ==  len(height) - 1:
                max_right[i] = height[len(height) - 1]
                continue
            max_right[i] = max(max_right[i+1], height[i])

        total = 0
        for i in range(len(height)):
            total += min(max_left[i], max_right[i]) - height[i]
        
        return total