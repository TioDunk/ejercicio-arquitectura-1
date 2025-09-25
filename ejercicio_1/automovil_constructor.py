from constructor import Constructor
from automovil import Automovil

class AutomovilConstructor(Constructor):
    _motor: str = ""
    _color: str = ""
    _llantas: str = ""
    _interiores: str = ""
    _techoSolar: bool = False
    _gps: bool = False


    def __init__(self) -> None:
        self.reiniciar()

    def reiniciar(self) -> Constructor:
        self._motor = ""
        self._color = ""
        self._llantas = ""
        self._interiores = ""
        self._techoSolar = False
        self._gps = False
        return self

    def conMotor(self, motor: str) -> Constructor:
        self._motor = motor
        return self

    def conColor(self, color: str) -> Constructor:
        self._color = color
        return self

    def conLlantas(self, llantas: int) -> Constructor:
        self._llantas = llantas
        return self

    def conInteriores(self, interiores: str) -> Constructor:
        self._interiores = interiores
        return self

    def conTechoSolar(self, techoSolar: bool) -> Constructor:
        self._techoSolar = techoSolar
        return self

    def conGPS(self, gps: bool) -> Constructor:
        self._gps = gps
        return self

    def construir(self) -> Automovil:
        automovil = Automovil(
            motor=self._motor,
            color=self._color,
            llantas=self._llantas,
            interiores=self._interiores,
            techoSolar=self._techoSolar,
            gps=self._gps,
        )
        self.reiniciar()
        return automovil