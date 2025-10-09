class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        # by how much i am shifting bits to the left
        power = 31

        print(f"start-------")  
        print(f"{n:032b}")  

        while n:
            print(f"loop-------")  
            # extract LSB of n (0 or 1). move that bit into the power position in res.
            res += (n & 1) << power
            print(f"res: {res:032b}")  

            n = n >> 1 # drop the bit we just used (shift n right by 1).
            print(f"n. : {n:032b}")  

            # move one position right in ret for the next write.
            power -= 1
        
        print(f"final: {res:032b}")  

        return res

#T:O(1)
#S:O(1)
