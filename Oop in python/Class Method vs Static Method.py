class Math:
    @staticmethod
    def add(x, y):
        return x + y

    @classmethod
    def identity(cls):
        return f"This is {cls.__name__}"

# Test
print(Math.add(2, 3))         # 5
print(Math.identity())        # Math
