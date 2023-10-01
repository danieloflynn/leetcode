
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        sol = []
        for idx, (i, j) in enumerate(zip(l1[::-1], l2[::-1])):
            sol.append((i + j) % 10)
            if (i + j)//10:
                sol[idx - 1] += 1

        sol.reverse()
        return sol


sol = Solution()

print(sol.addTwoNumbers([2, 4, 3], [5, 6, 4]))
