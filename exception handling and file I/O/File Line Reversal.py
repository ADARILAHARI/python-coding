def reverse_file_lines(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    with open(filename, 'w') as f:
        for line in reversed(lines):
            f.write(line)

# Test
# reverse_file_lines('sample.txt')
