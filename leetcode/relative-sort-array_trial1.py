class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1.sort()

        arr1Dict = {}

        for num in arr1:
            if num not in arr1Dict:
                arr1Dict[num] =1
            else:
                arr1Dict[num] +=1
        
        result=[]

        for num in arr2:
            if num in arr1Dict:
                result += arr1Dict[num] * [num]
                arr1Dict.pop(num)
        
        if arr1Dict:
            for key,value in arr1Dict.items():
                result += value * [key]
        
        return result