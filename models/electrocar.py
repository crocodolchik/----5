from .vehicle import Vehicle

class ElectroCar(Vehicle):
    def __init__(self, brand, model, year, battery_capacity):

        super().__init__(brand, model, year)

        self.battery_capacity = battery_capacity

    
    def get_info(self):
        return f"Электромоб: {super().get_info()}, батарея: {self.battery_capacity} кВтч"

  
    def move(self):
        return f"{self.brand} {self.model} едет бесшумно на элек. тяге"