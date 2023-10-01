class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        q, r = divmod(len(x), 2)

        if r == 1:
            p = q
        else:
            p = q - 1
        for i in range(1, q+1):
            print(p + i)
            print(q - i)
            if x[p+i] != x[q-i]:
                return False
        return True


sol = Solution()

sol.isPalindrome(123321)
