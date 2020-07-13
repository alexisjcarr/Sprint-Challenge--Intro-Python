# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


class Vehicle:
    """
    base class
    """
    pass


class FlightVehicle(Vehicle):
    """
    child class of Vehicle
    """
    pass


class Starship(FlightVehicle):
    """
    child class of FlightVehicle
    """
    pass


class Airplane(FlightVehicle):
    """
    child class of FlightVehicle
    """
    pass


class GroundVehicle(Vehicle):
    """
    child class of Vehicle
    """
    pass


class Car(GroundVehicle):
    """
    child class of GroundVehicle
    """
    pass


class Motorcycle(GroundVehicle):
    """
    child class of GroundVehicle
    """
    pass
