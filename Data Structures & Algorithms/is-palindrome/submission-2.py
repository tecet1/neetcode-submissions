import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        parsed = ""
        for c in s:
            if c.isalpha() or c.isdigit():
                parsed += c.upper()
        print(parsed)

        if parsed == parsed[::-1]: return True
        return False