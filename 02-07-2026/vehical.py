'''Create a Vehicle base class with Brand and Model.
Create Car (Fuel Type) and Bike (Engine Capacity) child classes.
Override display() in child classes.
'''

class vehical:
    brand=""
    Model=""
    def __init__(self,brand,model):
        self.brand=brand
        self.Model=model
class car(vehical):
    fueltype=""
    def __init__(self, brand, model,fuel):
        super().__init__(brand, model)
        self.fueltype=fuel
        
        def display(self):
            print()
        
class bike(vehical):
    fueltype=""
    def __init__(self, brand, model,fuel):
        super().__init__(brand, model)
        self.fueltype=fuel