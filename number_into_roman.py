class Solution(object):
    def intToRoman(self, num, output=""):
        """
        :type num: int
        :rtype: str
        """

        roman = [["M", 1000], ["CM", 900], ["D", 500], ["CD", 400], ["C", 100], ["XC", 90], [
            "L", 50], ["XL", 50], ["X", 10], ["IX", 9], ["V", 5], ["IV", 1], ["I", 1]]

        for i in range(len(roman)):
            while num >= roman[i][1]:
                num -= roman[i][1]
                output += roman[i][0]
        return output


sol = Solution()
sol.intToRoman(3)
