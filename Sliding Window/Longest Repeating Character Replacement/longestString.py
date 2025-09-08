class Solution:
    def longestString(self, s: str, k: int) -> int: 
        left = 0
        count = [0] * 26
        length = float("-inf")

        for right in range(len(s)):
            count[ord(s[right]) - ord('A')] += 1

            while (right - left + 1) - max(count) > k:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1
            
            length = max(length, (right - left + 1))
        
        return length if length != float(-"inf") else 0

