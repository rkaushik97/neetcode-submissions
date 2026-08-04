class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        char_set = set()
        result = 0
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[r])
            result = max(result, r-left+1)
        return result