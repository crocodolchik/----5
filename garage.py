class Garage:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def remove_vehicle(self, vehicle):
        if vehicle in self.vehicles:
            self.vehicles.remove(vehicle)

    def show_all(self):
        if not self.vehicles:
            print("Гараж пуст.")
        for v in self.vehicles:
            print(v.get_info())

    def find_by_brand(self, brand):
        return [v for v in self.vehicles if v.brand.lower() == brand.lower()]