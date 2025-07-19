class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        return f"Engine started{self.horsepower}"

class Car:  # Car HAS-A Engine
    def __init__(self, make, model, horsepower):
        self.make = make
        self.model = model
        self.engine = Engine(horsepower)  # Composition
    
    def start(self):
        return f"{self.make} {self.model}: {self.engine.start()}"

# Usage
car = Car("Toyota", "Camry", 200)
print(car.start())  # "Toyota Camry: Engine started"