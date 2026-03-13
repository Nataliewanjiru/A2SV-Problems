class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set("aeiou")
        res = 0
        n = len(word)
        
        for i in range(n):
            current_substring_vowels = set()
            for j in range(i, n):
                if word[j] not in vowels:
                    break
                
                current_substring_vowels.add(word[j])
                
                if len(current_substring_vowels) == 5:
                    res += 1
        return res
