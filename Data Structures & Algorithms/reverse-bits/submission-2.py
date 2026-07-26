class Solution:

    
    def reverseBits(self, n: int) -> int:
        
        bitIndex = 0
        maxBits = 32
        newNumb = 0

        binval = 0b1010
        
        while(bitIndex < maxBits):
            bit_mask = 1 << bitIndex
            neg_bit_mask = 1 << (31 - bitIndex)
            currBit = bit_mask & n

            if(currBit):
                newNumb = newNumb | neg_bit_mask
                print ("newNumb",f"{newNumb:032b}")
            
            bitIndex += 1

        return newNumb