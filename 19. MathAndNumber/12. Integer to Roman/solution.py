class Solution:
    def intToRoman(self, num: int) -> str:
        roman_map = {
            "M":	1000,
            "CM":   900,
            "D":	500,
            "CD":   400,
            "C":	100,
            "XC":   90,
            "L":	50,
            "XL":   40,
            "X":	10,
            "IX":   9,
            "V":	5,
            "IV":   4,
            "I":	1,
        }

        remainder = num
        roman = ""
        for key in roman_map:
            value = roman_map[key]
            while value <= remainder:
                roman += key
                remainder = remainder - value
            
        return roman
    
#T:O(n)
#S:O(1)