class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        arr1= []

        i,j=0,len(skill)-1

        while i < j:
            s = [skill[i],skill[j]]
            arr1.append(s)
            i += 1
            j -= 1
        
        
        result = 0
        num = sum(arr1[0])

        for i in arr1:
            m = math.prod(i)
            s = sum(i)
            if s == num :
               result += m
            else:
                return -1

        return result