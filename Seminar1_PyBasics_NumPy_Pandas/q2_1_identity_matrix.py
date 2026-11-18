# Create a 5x5 identity matrix and print it.

identity_matrix = []
for i in range(5):
    row = []
    for j in range(5):
        if i == j:
            row.append(1)
        else:
            row.append(0)
    identity_matrix.append(row)
# Print identity matrix
for row in identity_matrix:
    print(row)
