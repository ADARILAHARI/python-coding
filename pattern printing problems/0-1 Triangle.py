n = 5
for i in range(n):
    for j in range(i + 1):
        print((i + j) % 2, end="")
    print()

'''
1
01
101
0101
10101
'''