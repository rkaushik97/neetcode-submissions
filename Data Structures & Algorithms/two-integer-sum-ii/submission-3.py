class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftIdx = 0
        rightIdx = len(numbers) - 1

        while leftIdx < rightIdx:
            addition = numbers[leftIdx] + numbers[rightIdx]
            if addition == target:
                return [leftIdx + 1, rightIdx + 1]
            
            if addition > target:
                rightIdx -= 1
                
            if addition < target:
                leftIdx += 1
                
        return []