class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return
        
        rows, cols = len(matrix), len(matrix[0])
        self.sums = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        for r in range(rows):
            for c in range(cols):
                self.sums[r + 1][c + 1] = (matrix[r][c] + 
                                         self.sums[r][c + 1] + 
                                         self.sums[r + 1][c] - 
                                         self.sums[r][c])

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        return (self.sums[r2 + 1][c2 + 1] - 
                self.sums[r1][c2 + 1] - 
                self.sums[r2 + 1][c1] + 
                self.sums[r1][c1])


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)