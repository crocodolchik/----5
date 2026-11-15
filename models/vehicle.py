from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self._speed = 0

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        if value < 0:
            raise ValueError("Скрст не может быть отрицательной")
        self._speed = value

    def accelerate(self, value):
        self.speed = self._speed + value

    def brake(self, value):
        new_speed = self._speed - value
        self.speed = new_speed if new_speed >= 0 else 0

    def stop(self):
        self.speed = 0

    def get_info(self):
        return f"{self.brand} {self.model} ({self.year}), скорость: {self._speed}"

    def __str__(self):
        return self.get_info()

    @abstractmethod
    def move(self):
        pass