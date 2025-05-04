class AgeTooSmallError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise AgeTooSmallError("Age must be at least 18")
    return "Age is valid"

# Test
# print(check_age(15))  # Will raise exception
