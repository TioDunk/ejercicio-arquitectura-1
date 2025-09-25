from dataclasses import dataclass

@dataclass(frozen=True)
class Automovil:
    motor: str = ""
    color: str = ""
    llantas: str = ""
    interiores: str = ""
    techoSolar: bool = False
    gps: bool = False
        
