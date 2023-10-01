class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ""
        for i in range(len(s)):
            # odd
            odd = self.check(s, i-1, i+1)

        # even
            even = self.check(s, i, i+1)
            if len(odd) > len(longest):
                longest = odd

            if len(even) > len(longest):
                longest = even

        print(even)
        print(odd)

    def check(self, s, down, up):
        l = len(s)
        stop = 0
        while down >= 0 and up <= l and stop == 0:
            if s[down] == s[up]:
                down -= 1
                up += 1
                continue
            stop = 1

        return s[down:up]


sol = Solution()

sol.longestPalindrome("aacabdkacaa")
