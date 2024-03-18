import pytest
from exceptions import (LowFuelError, NotEnoughFuel, CargoOverload)
from main import Car, Engine, Plane


def test_create_car():
    car = Car(1500, 40, 7)

    assert isinstance(car, Car)


def test_engine_is_not_car():
    engine = Engine(1800, 8)

    assert not isinstance(engine, Car)


def test_car_has_engine():
    car = Car(1500, 40, 7)
    engine = Engine(1800, 8)
    car.set_engine(engine)

    assert car.engine == engine


def test_raise_low_fuel_exception():
    car = Car(1200, 0, 7)

    with pytest.raises(LowFuelError) as e:
        car.start()
        assert True


def test_raise_not_enough_fuel():
    car = Car(1200, 10, 7)

    with pytest.raises(NotEnoughFuel) as e:
        car.move(200)
        assert True


def test_raise_overload_cargo_into_plane():
    plane = Plane()

    with pytest.raises(CargoOverload) as e:
        plane.load_cargo(15000)
        assert True


def test_check_remove_all_cargo():
    plane = Plane()
    plane.cargo = 1000

    prev_value = plane.cargo
    plane.load_cargo(4000)

    assert plane.cargo == 5000

    plane.remove_all_cargo()

    assert plane.cargo == prev_value

