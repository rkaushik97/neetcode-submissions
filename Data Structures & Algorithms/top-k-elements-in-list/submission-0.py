class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        look_up = {}
        for num in nums:
            if num in look_up:
                look_up[num] += 1
            else:
                look_up[num] = 1
        # now sort the dictionary based on value
        return sorted(look_up, key=look_up.get, reverse=True)[:k]