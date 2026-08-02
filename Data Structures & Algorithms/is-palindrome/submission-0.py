class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_chars = []
        for char in s:
            if char.isalnum():
                cleaned_chars.append(char.lower())
        cleaned_string = "".join(cleaned_chars)

        # two pointer
        leftidx = 0
        rightidx = len(cleaned_string) - 1
        while leftidx < rightidx:
            if cleaned_string[leftidx] == cleaned_string[rightidx]:
                leftidx += 1
                rightidx -= 1
            else:
                return False
        return True