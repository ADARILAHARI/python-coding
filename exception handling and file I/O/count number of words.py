def count_words(filename):
    try:
        with open(filename, 'r') as f:
            text = f.read()
            return len(text.split())
    except FileNotFoundError:
        return 0

# Test
# print(count_words('sample.txt'))
