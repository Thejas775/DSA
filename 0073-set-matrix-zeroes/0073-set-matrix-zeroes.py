class Solution(object):
    def setZeroes(self, matrix):
        new=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    new.append((i,j))
                    
        for each in new:
            for i in range(len(matrix)):
                matrix[i][each[1]] = 0
                
            for j in range(len(matrix[0])):
                matrix[each[0]][j]=0
                
        return matrix
                    
        