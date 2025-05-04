def process_input(val):
    try:
        return int(val)
    except ValueError:
        return "Invalid number"
    except TypeError:
        return "NoneType not allowed"

# Test
print(process_input("abc"))  # Output: Invalid number
