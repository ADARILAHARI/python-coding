def read_file(filename):
    try:
        with open(filename, 'r') as f:
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print("File not found.")

# Test
# read_file('sample.txt')
