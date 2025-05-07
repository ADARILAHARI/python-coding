rows, cols = 4, 5
for i in range(rows):
    if i == 0 or i == rows - 1:
        print("*" * cols)
    else:
        print("*" + " " * (cols - 2) + "*")

'''
Input: 4 5
Output:
*****
*   *
*   *
*****

'''