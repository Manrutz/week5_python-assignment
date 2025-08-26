class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"{self.brand} {self.model}"

# Derived class (Inheritance)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)  # call parent constructor
        self.storage = storage
        self.battery = battery
    
    # Method: make a call
    def make_call(self, contact):
        return f"📞 Calling {contact} using {self.device_info()}..."
    
    # Method: check battery
    def check_battery(self):
        return f"🔋 Battery at {self.battery}%"

# Create objects
phone1 = Smartphone("Apple", "iPhone 15", "256GB", 85)
phone2 = Smartphone("Samsung", "Galaxy S24", "512GB", 65)

# Test methods
print(phone1.device_info())
print(phone1.make_call("Alice"))
print(phone1.check_battery())

print(phone2.device_info())
print(phone2.make_call("Bob"))
print(phone2.check_battery())