class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        count = 0
        vowels = {"a", "e", "i", "o", "u"}
        n = len(word)
        for i in range(n):
            if word[i] not in vowels:
                continue
            
            sett = set()

            for j in range(i, n):
                if word[j] not in vowels:
                    break
                
                sett.add(word[j])

                if len(sett) == len(vowels):
                    count += 1
        
        return count

# T:O(n**2)
# S:O(1), because the set size is fixed(max 5). Therefore, the space does not grow with input size. Hence O(1)
