class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i,j = 0,0
       
        g.sort()
        s.sort()

        count = 0

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                count += 1
                i+=1
                j+=1
            else:
                j += 1
        
        return count