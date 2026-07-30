class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)
        if m > n:
            return False
        
        target = [0] * 26
        for ch in s1:
            target[ord(ch) - ord('a')] += 1
        
        window = [0] * 26
        
        for right in range(n):
            window[ord(s2[right]) - ord('a')] += 1
            if right >= m:
                left_char = s2[right - m]
                window[ord(left_char) - ord('a')] -= 1
            if right >= m - 1:
                if window == target:
                    return True
        return False