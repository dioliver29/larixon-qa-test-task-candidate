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
    MAX_FUEL_CAPACITY = 100

    def __init__(self, consumption_per_100km: float):
        if not isinstance(consumption_per_100km, (int, float)):
            raise TypeError("Consumption must be a number.")
        if consumption_per_100km <= 0:
            raise ValueError("Consumption must be positive.")
        self._consumption = consumption_per_100km
        self._fuel = 0.0

    def fill_up(self, liters: float):
        if not isinstance(liters, (int, float)):
            raise TypeError("Fuel amount must be a number.")
        if liters <= 0:
            raise ValueError("Fuel amount must be positive.")
        self._fuel = min(self._fuel + liters, self.MAX_FUEL_CAPACITY)

    def drive(self, distance: float):
        if not isinstance(distance, (int, float)):
            raise TypeError("Distance must be a number.")
        if distance < 0:
            raise ValueError("Distance cannot be negative.")
        fuel_needed = (self._consumption * distance) / 100
        if fuel_needed > self._fuel:
            raise ValueError("Not enough fuel.")
        self._fuel -= fuel_needed

    def remaining_fuel(self) -> float:
        return self._fuel


class Track:
    MAX_FUEL_CAPACITY = 600
    MAX_TRAILERS = 4

    def __init__(self, trailer_consumption_per_100km: float, trailer_count: int):
        if not isinstance(trailer_consumption_per_100km, (int, float)):
            raise TypeError("Trailer consumption must be a number.")
        if not isinstance(trailer_count, int):
            raise TypeError("Trailer count must be an integer.")
        if trailer_consumption_per_100km <= 0:
            raise ValueError("Trailer consumption must be positive.")
        if trailer_count < 0 or trailer_count > self.MAX_TRAILERS:
            raise ValueError(f"Trailer count must be between 0 and {self.MAX_TRAILERS}.")
        self._trailer_consumption = trailer_consumption_per_100km
        self._trailer_count = trailer_count
        self._consumption = self._trailer_consumption * self._trailer_count
        self._fuel = 0.0

    def set_trailer_count(self, new_count: int):
        if not isinstance(new_count, int):
            raise TypeError("Trailer count must be an integer.")
        if new_count < 0 or new_count > self.MAX_TRAILERS:
            raise ValueError(f"Trailer count must be between 0 and {self.MAX_TRAILERS}.")
        self._trailer_count = new_count
        self._consumption = self._trailer_consumption * self._trailer_count

    def fill_up(self, liters: float):
        if not isinstance(liters, (int, float)):
            raise TypeError("Fuel amount must be a number.")
        if liters <= 0:
            raise ValueError("Fuel amount must be positive.")
        self._fuel = min(self._fuel + liters, self.MAX_FUEL_CAPACITY)

    def drive(self, distance: float):
        if not isinstance(distance, (int, float)):
            raise TypeError("Distance must be a number.")
        if distance < 0:
            raise ValueError("Distance cannot be negative.")
        fuel_needed = (self._consumption * distance) / 100
        if fuel_needed > self._fuel:
            raise ValueError("Not enough fuel.")
        self._fuel -= fuel_needed

    def remaining_fuel(self) -> float:
        return self._fuel