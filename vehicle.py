from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def fill_up(self, liters: int):
        pass

    @abstractmethod
    def drive(self, distance: float):
        pass

    @abstractmethod
    def remaining_fuel(self) -> float:
        pass 

class Car:
    MAX_FUEL_CAPACITY = 100  # максимум 100 литров

    def __init__(self, consumption_per_100km: float):
        if consumption_per_100km <= 0:
            raise ValueError("Consumption must be positive.")
        self._consumption = consumption_per_100km
        self._fuel = 0.0

    def fill_up(self, liters: float):
        if liters <= 0:
            raise ValueError("Fuel amount must be positive.")
        self._fuel = min(self._fuel + liters, self.MAX_FUEL_CAPACITY)

    def drive(self, distance: float):
        if distance < 0:
            raise ValueError("Distance cannot be negative.")
        fuel_needed = (self._consumption * distance) / 100
        if fuel_needed > self._fuel:
            raise ValueError("Not enough fuel.")
        self._fuel -= fuel_needed

    def remaining_fuel(self) -> float:
        return self._fuel


class Track:
    MAX_FUEL_CAPACITY = 600  # максимальное кол-во литров
    MAX_TRAILERS = 4         # макс кол-во трейлеров для одного трака

    def __init__(self, trailer_consumption_per_100km: float, trailer_count: int):
        if trailer_consumption_per_100km <= 0:
            raise ValueError("Trailer consumption must be positive.")
        if trailer_count < 0 or trailer_count > self.MAX_TRAILERS:
            raise ValueError(f"Trailer count must be between 0 and {self.MAX_TRAILERS}.")

        self._trailer_consumption = trailer_consumption_per_100km
        self._trailer_count = trailer_count
        self._consumption = self._trailer_consumption * self._trailer_count
        self._fuel = 0.0

    def set_trailer_count(self, new_count: int):
        if new_count < 0 or new_count > self.MAX_TRAILERS:
            raise ValueError(f"Trailer count must be between 0 and {self.MAX_TRAILERS}.")
        self._trailer_count = new_count
        self._consumption = self._trailer_consumption * self._trailer_count

    def fill_up(self, liters: float):
        if liters <= 0:
            raise ValueError("Fuel amount must be positive.")
        self._fuel = min(self._fuel + liters, self.MAX_FUEL_CAPACITY)

    def drive(self, distance: float):
        if distance < 0:
            raise ValueError("Distance cannot be negative.")
        fuel_needed = (self._consumption * distance) / 100
        if fuel_needed > self._fuel:
            raise ValueError("Not enough fuel.")
        self._fuel -= fuel_needed

    def remaining_fuel(self) -> float:
        return self._fuel

