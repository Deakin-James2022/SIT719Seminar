# Create a 12x12 matrix, in which the elements on the borders will be equal to 1, and inside 0.

matrix = []
for i in range(12):
    row = []
    for j in range(12):
        if i == 0 or i == 11 or j == 0 or j == 11:
            row.append(1)
        else:
            row.append(0)
    matrix.append(row)
# Print matrix
for row in matrix:
    print(row)
