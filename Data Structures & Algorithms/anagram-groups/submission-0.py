class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        look_up = {}
        for word in strs:
            canonical_form = "".join(sorted(word))
            if canonical_form in look_up:
                look_up[canonical_form].append(word)
            else:
                look_up[canonical_form] = [word]
        return list(look_up.values())