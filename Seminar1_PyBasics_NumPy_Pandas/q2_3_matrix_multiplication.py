# Please multiply two matrix of same size. num1 = [[10, 20, 30], [4, 8, 9]]; num2 = [[14, 26, 3], [2, 3, 10]]

num1 = [[10, 20, 30], [4, 8, 9]]
num2 = [[14, 26, 3], [2, 3, 10]]
result = []
for i in range(len(num1)):
    row = []
    for j in range(len(num1[i])):
        row.append(num1[i][j] * num2[i][j])
    result.append(row)
print("Result of matrix multiplication:")
for row in result:
    print(row)
