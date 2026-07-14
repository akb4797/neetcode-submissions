# #O(n2)
# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         for elem_left in range(0, len(nums)):

#             for elem_inner in range(elem_left+1, len(nums)):           

#                 if(nums[elem_left] == nums[elem_inner]):
#                     return True

#         return False


# O(1)
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seenSet = set()

        for elem in nums:
            if elem in seenSet:
                return True
            else:
                seenSet.add(elem)

        return False


# O(1)  Pro
# return len(nums) != len(set(nums))
  

