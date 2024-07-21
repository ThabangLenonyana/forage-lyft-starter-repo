from abc import ABC, abstractmethod
from serviceable import Serviceable


class Engine(Serviceable):

    @abstractmethod
    def needs_service(self):
        pass


class SternmanEngine(Engine):
    def __init__(self, warning_light_is_on):
        self.__warning_light_is_on = warning_light_is_on

    def needs_service(self):
        if self.__warning_light_is_on:
            return True
        else:
            return False


class WilloughbyEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage):
        self.__current_mileage = current_mileage
        self.__last_service_mileage = last_service_mileage

    def engine_should_be_serviced(self):
        return self.__current_mileage - self.__last_service_mileage > 60000


class CapuletEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage):
        self.__current_mileage = current_mileage
        self.__last_service_mileage = last_service_mileage

    def needs_service(self):
        return self.__current_mileage - self.__last_service_mileage > 30000
