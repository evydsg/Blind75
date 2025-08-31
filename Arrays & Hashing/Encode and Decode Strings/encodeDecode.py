class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        encoded = ""

        for string in strs:
            len_string = len(string)
            encoded += str(len(string))+"*"+string
        
        return encoded

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        
        decoded = []
        ptr1 = 0

        while ptr1 < len(s):
            ptr2 = ptr1
            len_string = ""

            while s[ptr2] != '*' and ptr2 < len(s):
                len_string += s[ptr2]
                ptr2 += 1
            
            length = int(len_string)
            start = ptr2 + 1
            end = start + length
            string = s[start: end]
            decoded.append(string)

            ptr1 = end

        return decoded