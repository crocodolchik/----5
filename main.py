from models.car import Car
from models.truck import Truck
from models.motorcycle import Motorcycle
from garage import Garage
from models.electrocar import ElectroCar

def main():
    car = Car("Lamborghini ", "Urus", 2017, 2)
    truck = Truck("Rig ", "FH16", 2022, 4)
    moto = Motorcycle("TMBK Ninja 400cc", "R1", 2022, False)
    electro = ElectroCar("Tesla", "Model s", 2023, 75)

    car.accelerate(120)
    car.brake(10)
    car.stop()
    
    vehicles = [car, truck, moto, electro]
    for v in vehicles:
        print(v.move())
        print(v.get_info())
        print("-" * 20)

    garage = Garage()
    garage.add_vehicle(car)
    garage.add_vehicle(truck)
    garage.add_vehicle(moto)
    garage.add_vehicle(electro)
    
    print("\n--- Содержимое гаража ---")
    garage.show_all()

    print("\n--- Поиск по марке 'Lamborghini' ---")
    found = garage.find_by_brand("Lamborghini")
    for v in found:
        print(v.get_info())

if __name__ == "__main__":
    main()