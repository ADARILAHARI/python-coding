def read_large_file(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()

# Usage
# for line in read_large_file('bigfile.txt'):
#     print(line)

