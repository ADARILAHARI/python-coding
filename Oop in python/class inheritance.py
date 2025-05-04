class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Dog barks"

# Test
d = Dog()
print(d.speak())  # Output: Dog barks
