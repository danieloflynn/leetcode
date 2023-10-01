class Solution:
    def myAtoi(self, s: str) -> int:

        s = s.strip()
        if len(s) == 0:
            return 0

        sign = 1
        if s[0] == "+":
            s = s[1:]
        elif s[0] == "-":
            sign = -1
            s = s[1:]

        x = 0
        for c in s:
            if not c.isdigit():
                break
            else:
                x = x*10 + int(c)
        x = sign * x
        max = 2**31 - 1
        min = -1*2**31
        if x > max:
            return max
        if x < min:
            return min
        return x


sol = Solution()
sol.myAtoi("   -04f")
