class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:
        
        '''
        1. Transpose matrix
        2. reverse each row
        
        '''

        assert (1 == 1)

        n = len(matrix[0])
        for row in range(0,n):
            for col in range(row+1,n):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
            
        print ("transposed:", str(matrix))  

        for row in range(0,n):
            print ("\nrow:",str(matrix[row]))

            for col in range(0,n//2):
                print ("col:", col)
                print ("n-1-col:", n-1-col)

                matrix[row][col], matrix[row][n-1-col] = matrix[row][n-1-col], matrix[row][col]
                
        print ("rotated:", str(matrix))  
            