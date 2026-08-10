class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        hash_map_s1 = {}
        
        for s in s1:
            hash_map_s1[s] = hash_map_s1.get(s, 0) + 1
        
        for i in range(len(s2)+1):
            window = s2[i : i+len(s1)] # lec
            hash_map_s2 = {}
            for s in window:
                hash_map_s2[s] = hash_map_s2.get(s, 0) + 1    
            if hash_map_s1 == hash_map_s2:
                return True
        return False