def write_to_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')

# Test
# write_to_file('output.txt', ['Hello', 'World'])
