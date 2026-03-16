class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels_array = ['a', 'e', 'i', 'o','u']

        window_array = []

        s_array = []

        left = 0
        
        res = 0

        n = len(s)

        for right in range(n):
            letter = s[right]
            s_array.append(letter)

            if letter in vowels_array:
                window_array.append(letter)
          
            if len(s_array) > k:
                letter = s[left]
                s_array.remove(letter)

                if letter in window_array:
                    window_array.remove(letter)
                left += 1
            
            if len(s_array) == k:
                n = len(window_array)
                res = max(res,n)
        
        return res

                       