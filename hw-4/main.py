from exceptions import LowFuelError, NotEnoughFuel, CargoOverload
from dataclasses import dataclass
from abc import ABC


class Vehicle(ABC):
    weight = 0
    started = False
    fuel = 0
    fuel_consumption = 7

    def __init__(self, weight=None, fuel=None, fuel_consumption=None):
        if weight:
            self.weight = weight
        if fuel:
            self.fuel = fuel
        if fuel_consumption:
            self.fuel_consumption = fuel_consumption

    def start(self):
        if self.fuel > 0:
            self.started = True
        else:
            raise LowFuelError

    def move(self, distance: float):
        required_fuel = self.fuel_consumption * distance / 100
        if required_fuel > self.fuel:
            raise NotEnoughFuel


@dataclass
class Engine:
    volume: float
    pistons: int


class Car(Vehicle):
    engine: Engine = None

    def __init__(self, weight, fuel, fuel_consumption):
        super().__init__(weight, fuel, fuel_consumption)

    def set_engine(self, engine: Engine):
        self.engine = engine


class Plane(Vehicle):
    cargo: int = 0
    prev_cargo: int = 0
    max_cargo: int = 7500

    def __init__(self, weight=None, fuel=None, fuel_consumption=None, max_cargo=None):
        super().__init__(weight, fuel, fuel_consumption)
        if max_cargo:
            self.max_cargo = max_cargo

    def load_cargo(self, cargo: int):
        new_cargo = self.cargo + cargo
        if new_cargo > self.max_cargo:
            raise CargoOverload
        self.prev_cargo = self.cargo
        self.cargo = new_cargo

    def remove_all_cargo(self):
        self.cargo = self.prev_cargo
