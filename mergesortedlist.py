class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = []
        while nums1 and nums2:
            if nums1[0] > nums2[0]:
                merged.append(nums2[0])
                nums2.pop(0)
            else:
                merged.append(nums1[0])
                nums1.pop(0)

        merged += nums1
        merged += nums2
        listlen = len(merged)
        nl = listlen//2
        if listlen % 2 == 0:

            return (float(merged[nl-1]) + (float(merged[nl])))/2
        else:

            return merged[nl]


sol = Solution()

sol.findMedianSortedArrays([1, 2], [3, 4])


# class Solution(object):
#     def findMedianSortedArrays(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: float
#         """
#         merged = []
#         for i, m in enumerate(nums1):
#             for j, n in enumerate(nums2):
#                 if m > n:
#                     print(m)
#                     print(n)
#                     merged.append(n)
#
#                 else:
#                     print("nums1 {}".format(m))
#                     print("nums2 {}".format(n))

#                     print("j {}".format(j))
#                     if (j != 0):
#                         nums2.pop(j-1)
#                     pass
#             print(m)
#             merged.append(m)
#

#
#         print(nums2)
#         merged += nums2
#
#         listlen = len(merged)
#         nl = listlen//2
#         if listlen % 2 == 0:
#
#             return (float(merged[nl-1]) + (float(merged[nl])))/2
#         else:
#
#             return merged[nl]
