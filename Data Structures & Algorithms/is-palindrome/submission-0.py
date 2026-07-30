class Solution:
    def isPalindrome(self, s: str) -> bool:
        forw = [char for char in s.lower() if char.isalnum()]
        backw = forw[::-1]
        if forw == backw:
            return True
        return False