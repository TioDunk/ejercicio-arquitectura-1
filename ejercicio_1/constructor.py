
from automovil import Automovil
from abc import ABC, abstractmethod

class Constructor(ABC):

    @abstractmethod
    def reiniciar(self) -> "Constructor":
        pass

    @abstractmethod
    def conMotor(self, motor: str) -> "Constructor":
        pass

    @abstractmethod
    def conColor(self, color: str) -> "Constructor":
        pass

    @abstractmethod
    def conLlantas(self, llantas: str) -> "Constructor":
        pass

    @abstractmethod
    def conInteriores(self, interiores: str) -> "Constructor":
        pass

    @abstractmethod
    def conTechoSolar(self, techoSolar: bool) -> "Constructor":
        pass

    @abstractmethod
    def conGPS(self, gps: bool) -> "Constructor":
        pass

    @abstractmethod
    def construir(self) -> Automovil:
        pass