class Vehicle:
    def move(self):
        pass  # abstract idea (to be overridden)

class Car(Vehicle):
    def move(self):
        return "🚗 Driving on the road"

class Plane(Vehicle):
    def move(self):
        return "✈️ Flying in the sky"

class Boat(Vehicle):
    def move(self):
        return "⛵ Sailing on the water"

# Create objects
vehicles = [Car(), Plane(), Boat()]

# Demonstrate polymorphism
for v in vehicles:
    print(v.move())