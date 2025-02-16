class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        top =0
        bottom = m-1
      
        while top<=bottom:
            half = (top + bottom) // 2
            midArray = matrix[half]
            poi1 = 0
            poi2 = n-1
            if target > midArray[poi2]:
                top = half +1
            elif target < midArray[poi1]:
                bottom = half - 1
            else:
                for i in range(n):
                    if target== midArray[i]:
                        return True
                return False
        return False


                 




        