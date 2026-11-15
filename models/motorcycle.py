from .vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, has_sidecar):
        super().__init__(brand, model, year)
        self.has_sidecar = has_sidecar

    def get_info(self):
        sidecar = "с коляской" if self.has_sidecar else "без коляски"
        return f"Мотик: {super().get_info()}, {sidecar}"

    def move(self):
        return f"{self.brand} {self.model} мчится по шоссе."