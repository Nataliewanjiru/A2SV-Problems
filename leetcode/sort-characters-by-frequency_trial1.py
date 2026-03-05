class Solution:
    def frequencySort(self, s: str) -> str:
        s_dict = {}

        for i in s:
            if i not in s_dict:
                s_dict[i] = 1
            else:
                s_dict[i] +=1
        
        n = sorted(s_dict.items(), key=lambda x: -x[1])
        
        result = "".join(c * v for c ,v in n)

        return result
        
       