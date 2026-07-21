class Solution:
    def hammingWeight(self, n: int) -> int:
        
        inpBin = f"{n:032b}"
        print ("inpBin:", inpBin)

        ctr = 0
        val = 0
        oneCount = 0

        while(ctr<32):
            val = n & (1<<ctr)

            if(val):
                oneCount += 1

            ctr += 1

        return oneCount