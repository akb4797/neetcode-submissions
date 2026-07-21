class Solution:

    
    def reverseBits(self, n: int) -> int:
        
        bitIndex = 0
        maxBits = 32
        newNumb = 0

        while(bitIndex < maxBits):
            bit_mask = 1 << bitIndex
            neg_bit_mask = 1 << (31 - bitIndex)
            # print ("bit_mask",bit_mask)
            currBit = bit_mask & n
            print ("bitIndex",bitIndex)
            # print ("currBit",currBit)

            if(currBit):
                newNumb = newNumb | neg_bit_mask
                print ("newNumb",f"{newNumb:032b}")
            
            bitIndex += 1

        return newNumb