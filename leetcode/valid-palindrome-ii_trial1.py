class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        
        while i < j:
            if s[i] != s[j]:
                left1, right1 = i + 1, j
                while left1 < right1 and s[left1] == s[right1]:
                    left1 += 1
                    right1 -= 1
                
                left2, right2 = i, j - 1
                while left2 < right2 and s[left2] == s[right2]:
                    left2 += 1
                    right2 -= 1
                
                return left1 >= right1 or left2 >= right2
            
            i += 1
            j -= 1
        
        return True