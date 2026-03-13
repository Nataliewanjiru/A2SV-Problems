class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)
        
        res= []

        s_count = Counter()
        p_count = Counter(p)

        for i in range(n):
            s_count[s[i]] += 1

            if i >= m:
                l_char = s[i-m]
                s_count[l_char] -= 1
                if s_count[l_char] == 0:
                    del s_count[l_char]

            if p_count == s_count:
                res.append(i- m + 1)
            
        return res


        