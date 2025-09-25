from constructor import Constructor
from automovil import Automovil

class Concesionario:
    def construirSUV(self, constructor: Constructor) -> Automovil:
        constructor.conColor("#008000")
        constructor.conGPS(True)
        constructor.conMotor("V4 - 1.6L")
        constructor.conTechoSolar(True)
        return constructor.construir()
    
    def construirDeportivo(self, constructor: Constructor) -> Automovil:
        constructor.conColor("#B81518")
        constructor.conMotor("V8 - 4L")
        constructor.conLlantas("Michelin")
        constructor.conInteriores("cuero")
        return constructor.construir()
    
    def construirBasico(self, constructor: Constructor) -> Automovil:
        constructor.conColor("#636363")
        constructor.conMotor("V4 - 1.5L")
        return constructor.construir()