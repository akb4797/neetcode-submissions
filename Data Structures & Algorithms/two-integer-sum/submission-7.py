class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        #Logic for creating val-index mapping
        indx_list = []
        
        indx_ctr = 0
        for item in nums:
            indx_list.append([indx_ctr, item])
            indx_ctr += 1


        print ("indx_list:", indx_list)


        sorted_structure = sorted(indx_list, key = lambda x:x[1])

        print ("sorted:", sorted_structure)

        l_ptr = 0
        r_ptr = len(nums)-1

        while(r_ptr > l_ptr):

            if( sorted_structure[l_ptr][1] + sorted_structure[r_ptr][1] == target):
                return [min(sorted_structure[l_ptr][0], sorted_structure[r_ptr][0]), max(sorted_structure[l_ptr][0], sorted_structure[r_ptr][0])]
            elif(sorted_structure[l_ptr][1] + sorted_structure[r_ptr][1] > target):                
                r_ptr -= 1
            elif(sorted_structure[l_ptr][1] + sorted_structure[r_ptr][1] < target):                
                l_ptr += 1
    
        return [0, 0]



                    

