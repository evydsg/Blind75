def validPalindrome(s: str) -> bool:
    left = 0
    right = len(s)-1

    while left < right:
        if not(s[left].isalnum()):
            left += 1
            continue
        elif not(s[right].isalnum()):
            right -= 1
            continue
        else:
            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
    
    return True

s = "Was it a car or a cat I saw?"

print(validPalindrome(s))