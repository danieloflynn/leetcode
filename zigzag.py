class Solution:
    def convert(self, s: str, numRows: int) -> str:
        sl = len(s)
        if sl < numRows or numRows == 1:
            return s
        rows = ["" for _ in range(numRows)]
        # num of letters per row = 2(numRows - 1)
        # num of iterations needed = sl//(2(numRows - 1))
        # rem= sl%(2(numRows-1))
        q, r = divmod(sl, 2*(numRows - 1))

        for qq in range(q):
            # Down
            for i in range(numRows):
                rows[i] += s[qq*2*(numRows - 1) + i]
            # Up
            for j, i in enumerate(range(numRows-2, 0, -1)):
                rows[i] += s[qq*2*(numRows - 1) + (numRows - 1) + j + 1]
        # Down rem
        for i in range(min(numRows, r)):
            rows[i] += s[q*2*(numRows - 1) + i]
        # Up rem
        if (numRows < r):
            for j, i in enumerate(range(numRows-2, numRows - 2 - (r - numRows), -1)):
                a = q*2*(numRows - 1) + numRows + i - 1
                rows[i] += s[q*2*(numRows - 1) + numRows + j]

        final = "".join(rows)
        return final


sol = Solution()
sol.convert("PAYPALISHIRING", 4)

'''
Z A G
IZGIZG
G Z A

Z  Z  Z
I GI GI
GA GA G
Z  Z  Z

nRows down
nRows - 2 up starting Row(max - 1) ending Row(min + 1)

'''
