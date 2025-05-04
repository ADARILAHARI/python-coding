class Bird:
    def fly(self):
        return "Bird flies"

class Airplane:
    def fly(self):
        return "Airplane flies"

def lift_off(obj):
    print(obj.fly())

# Test
lift_off(Bird())       # Bird flies
lift_off(Airplane())   # Airplane flies
