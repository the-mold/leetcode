class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0

        signs = {"-","+"}
        sett = {"0","1","2","3","4","5","6","7","8","9"}
        n = len(s)

        INT_MAX = 2**31-1
        INT_MIN = -2**31

        start_idx = 0
        # skip spaces
        while start_idx < n:
            if s[start_idx] != " ":
                break
            start_idx += 1
        
        if start_idx >= n:
            return 0

        sign = 1
        # skip signs
        if s[start_idx] == "-":
            sign = -1
            start_idx += 1
        elif s[start_idx] == "+":
            sign = 1
            start_idx += 1

        result = 0
        for idx in range(start_idx, len(s)):
            char = s[idx]
            if char not in sett:
                break
            digit = int(char)

            if sign == 1 and (result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > 7)):
                return INT_MAX
            if sign == -1 and (result > abs(INT_MIN) // 10 or (result == abs(INT_MIN) // 10 and digit > 8)):
                return INT_MIN
            
            result = result * 10 + int(digit)
        
        return sign * result