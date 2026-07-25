# import math

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        '''
        1. a= sum to n natural numbers_ n*(n+1)/2
        2. b= sum of existing elem
        3. missing num = a-b
        '''

        n = len(nums)
        a = (n*(n+1))/2
        b = sum(nums)
        # mx = max(nums)
        # print (mx)
        missing = abs(b-a)
        return int(missing)
