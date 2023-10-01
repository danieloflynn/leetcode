class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if x[0] == "-":

            return int("-" + x[:0:-1])
        else:
            return int(x[::-1])


sol = Solution()
sol.reverse(-123)
