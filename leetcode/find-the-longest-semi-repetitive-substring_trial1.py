class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        max_len = 1
        left = 0
        last_pair_index = -1
        
        for right in range(1, len(s)):
            if s[right] == s[right - 1]:
                if last_pair_index != -1:
                    left = last_pair_index
                last_pair_index = right
            
            max_len = max(max_len, right - left + 1)
            
        return max_len
