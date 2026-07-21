class Solution:

    def hammingWeights(self, n: int) -> int:

        index = 0
        weight = 0
        val = n

        while(index < 32):
            bit_mask = (1 << index)
            if(val & bit_mask):
                weight += 1
            index += 1
        
        print ("curr weight:", weight)
        return weight
        
    def countBits(self, n: int) -> List[int]:
        
        outputList = []
        for elem in range(0, n+1):
            print ("elem", elem)
            outputList.append(self.hammingWeights(elem))
        
        return outputList
