class Solution:
    def groupAnagrams(self, words: List[str]) -> List[str]:
        anagrams = {}

        for word in words:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            
            count = tuple(count)

            if count in anagrams:
                anagrams[count].append(word)
            else:
                anagrams[count] = [word]
        
        return anagrams.values()