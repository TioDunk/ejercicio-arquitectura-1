#Beneficio1 y 2 -  Separamos las responsabilidades, este .py contine las plataformas a trabajar y si quiero agregar una nueva
#plataforma, replico la clase PlataformaNotificadora y agrego la nueva plataforma a trabajar, para el ejemplo Email
#Beneficio 3 - por este medio no necesito crear clases concretas para cada tipo de notificación y plataforma,
#solo creo las clases de notificación y las clases de plataforma y en test_escenario2.py las combino como quiera evitando
#la multiplicación de clases concretas

from abc import ABC, abstractmethod

class PlataformaNotificadora(ABC):
    @abstractmethod
    def dibujar(self, tipo: str, mensaje: str) -> None:
        pass

class PlataformaEscritorio(PlataformaNotificadora):
    def dibujar(self, tipo: str, mensaje: str) -> None:
        print(f"[ESCRITORIO] {tipo.upper()}: {mensaje}")

class PlataformaWeb(PlataformaNotificadora):
    def dibujar(self, tipo: str, mensaje: str) -> None:
        print(f"[WEB] {tipo.upper()}: {mensaje}")

class PlataformaMovil(PlataformaNotificadora):
    def dibujar(self, tipo: str, mensaje: str) -> None:
        print(f"[MOVIL] {tipo.upper()}: {mensaje}")

class PlataformaEmail(PlataformaNotificadora):
    def dibujar(self, tipo: str, mensaje: str) -> None:
        print(f"[EMAIL] {tipo.upper()}: {mensaje}")