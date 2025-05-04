class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, I am {self.name} and I am {self.age} years old."

# Test
p = Person("Alice", 25)
print(p.greet())
