class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_strings = []
        for string in strs:
            encoded_strings.append(str(len(string)) + "#" + string)
        return "".join(encoded_strings)

        
    def decode(self, s: str) -> List[str]:
        # 5#Hello5#World
        i = 0
        result = []
        while i < len(s):
            # find out the first occurance of # at the index end
            j = s.index("#", i)
            length = int(s[i:j])
            result.append(s[j + 1 : j + length + 1]) 
            i = j + 1 + length
        return result

