class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window=[]
        answer=0
        left=0
        
        for right in range(len(s)):
            while s[right] in window:
                window.pop(0)
                left += 1
            
            window.append(s[right])
            answer = max(answer, len(window))
        
        return answer