class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward = [char for char in s.lower() if char.isalnum()]
        backward = forward[::-1]
        if forward == backward:
            return True
        else:
            return False