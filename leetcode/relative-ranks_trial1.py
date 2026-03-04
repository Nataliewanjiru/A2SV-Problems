class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        s = sorted(score, reverse= True)
        s_dict = {}

        result = []

        for i in range(len(s)):
            if i == 0:
               s_dict[s[i]] = "Gold Medal"
            elif i == 1:
               s_dict[s[i]] = "Silver Medal"
            elif i == 2:
               s_dict[s[i]] = "Bronze Medal"
            else:
               s_dict[s[i]] =f"{i+1}"
       
        for i in score:
            result.append(s_dict[i])
        
        return result