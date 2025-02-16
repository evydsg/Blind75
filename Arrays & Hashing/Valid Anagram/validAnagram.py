class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict_s, dict_t = {}, {}

        for character in s:
            if character in dict_s:
                dict_s[character] += 1
            else:
                dict_s[character] = 1
        
        for character in t:
            if character in dict_t:
                dict_t[character] += 1
            else:
                dict_t[character] = 1
        
        return dict_s == dict_t