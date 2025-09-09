class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {'(' : ')', '{' : '}', '[' : ']'}
        valid = []

        for b in s:
            if b in bracket:
                valid.append(b)
            elif len(valid) != 0 and b == bracket[valid[-1]]:
                valid.pop()
            else:
                return False
        
        return len(valid) == 0