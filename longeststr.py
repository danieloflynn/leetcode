class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        str = ""
        for l in s:
            if l in str:

                newlen = len(str)
                if newlen > longest:
                    longest = newlen
                print(str)
                str = str[str.index(l)+1:]
                print(str)
            str += l

        newlen = len(str)
        if newlen > longest:
            longest = newlen
        return longest


sol = Solution()
sol.lengthOfLongestSubstring("aabaab!bb")
