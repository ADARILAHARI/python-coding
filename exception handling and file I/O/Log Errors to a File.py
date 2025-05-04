def log_error(err_msg, filename="error.log"):
    with open(filename, 'a') as f:
        f.write(err_msg + '\n')

# Usage
# try:
#     1 / 0
# except ZeroDivisionError as e:
#     log_error(str(e))
