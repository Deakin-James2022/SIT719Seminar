# Please create a list of tuples with numbers and their squares. Examples: Our input list is [1, 3, 5, 7, 9] after the operation the output would be [(1, 1), (3, 9), (5, 25), (7, 49), (9, 81)]. Hint: please use for loop.

numbers = [1, 3, 5, 7, 9]
squares = []
for num in numbers:
    squares.append((num, num ** 2))
print(squares)
