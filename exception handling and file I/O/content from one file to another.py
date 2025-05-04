def copy_file(source, dest):
    try:
        with open(source, 'r') as src, open(dest, 'w') as dst:
            dst.write(src.read())
    except FileNotFoundError:
        print("Source file not found.")

# Test
# copy_file('sample.txt', 'copy.txt')
