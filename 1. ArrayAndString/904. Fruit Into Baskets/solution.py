class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_length = 0
        l = 0
        hashmap = {}
        for r, fruit in enumerate(fruits):
            hashmap[fruit] = hashmap.get(fruit, 0) + 1

            # need to remove from basket
            while len(hashmap) > 2:
                hashmap[fruits[l]] -= 1

                if hashmap[fruits[l]] == 0:
                    del hashmap[fruits[l]]
                
                l+=1
            
            max_length = max(max_length, r - l + 1)
            
        return max_length

#T:O(n)
#S:O(1), because there are at most three items in the hashmap