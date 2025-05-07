n = 5
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("".join(str(j) for j in range(1, i + 1)), end="")
    print("".join(str(j) for j in range(i - 1, 0, -1)))

'''    
    1
   121
  12321
 1234321
123454321
'''