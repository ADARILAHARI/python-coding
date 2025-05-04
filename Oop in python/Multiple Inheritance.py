class A:
    def method(self):
        return "A"

class B:
    def method(self):
        return "B"

class C(A, B):
    pass

# Test
c = C()
print(c.method())  # Output: A (based on MRO)
