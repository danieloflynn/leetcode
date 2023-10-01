class Solution(object):
    def twoSum(self, nums, target):
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n

            if diff in prevMap:
                print(prevMap[diff])
                return (prevMap[diff], i)
            prevMap[n] = i
        return


sol = Solution()
print(sol.twoSum([1, 2, 4], 6))
