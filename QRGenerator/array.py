def set_zeroes(matrix):
    if not matrix or not matrix[0]:
        return
    
    rows , cols = len(matrix) , len(matrix[0])
    zero_rows = set()
    zero_cols = set()
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols .add(j)

    for i in zero_rows:
        for j in range(cols):
            matrix[i][j] = 0   

    for j in zero_cols:
        for i in range(rows):
            matrix[i][j] = 0
matrix = [
    [1,1,1],
    [1,0,1],
    [1,1,1]
]            
set_zeroes(matrix)
for row in matrix:
    print(row)
            









    
 









