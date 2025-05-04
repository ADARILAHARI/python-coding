class Student:
    count = 0

    def __init__(self):
        Student.count += 1

# Test
s1 = Student()
s2 = Student()
print(Student.count)  # Output: 2
