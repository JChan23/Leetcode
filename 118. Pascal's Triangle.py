import math
class Solution:
    def generate(self, rows: int) -> List[List[int]]:
       #initialise triangle
        triangle = []
        for i in range(rows):
            col = []
            counter = 0
            for j in range(i+1):
                if counter == 0 or counter == i:
                    col.append(1)
                else:
                    col.append(0)
                counter = counter + 1
            triangle.append(col)

        #filling in. Only need to start from row 3
        for i in range(2, rows):
            for j in range(1, len(triangle[i])-1):
                triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
        return triangle
