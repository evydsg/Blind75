class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        length = 0
        unique = set()
        left = 0

        for right in range(len(s)):

            while s[right] in unique:
                unique.remove(s[left])
                left += 1

            unique.add(s[right])
            length = max(len(unique), length)
        
        return length