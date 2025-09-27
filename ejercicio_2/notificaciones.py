#Beneficio1 y 2 -  Separamos las responsabilidades, este .py contine las notificaciones a trabajar y si quiero agregar una nueva
#notificación, agrego una nueva clase que herede de Notificacion y la implemento para el ejemplo NotitificacionError
#Beneficio 3 - por este medio no necesito crear clases concretas para cada tipo de notificación y plataforma,
#solo creo las clases de notificación y las clases de plataforma y en test_escenario2.py las combino como quiera evitando
#la multiplicación de clases concretas

from plataformas import PlataformaNotificadora
from abc import ABC, abstractmethod

class Notificacion(ABC):
    def __init__(self, plataforma: PlataformaNotificadora, mensaje: str) -> None:
        self._plataforma = plataforma
        self._mensaje = mensaje

    def set_plataforma(self, plataforma: PlataformaNotificadora) -> None:
        print(f"Cambiando plataforma de notificación a: {type(plataforma).__name__}")
        self._plataforma = plataforma

    @abstractmethod
    def mostrar(self) -> None:
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

class NotificacionMensaje(Notificacion):
    def mostrar(self) -> None:
        print("Mostrando notificación de mensaje:")
        self._plataforma.dibujar("Mensaje", self._mensaje)

class NotificacionAlerta(Notificacion):
    def mostrar(self) -> None:
        print("Mostrando notificación de alerta:")
        self._plataforma.dibujar("Alerta", self._mensaje)

class NotificacionConfirmacion(Notificacion):
    def mostrar(self) -> None:
        print("Mostrando notificación de confirmación:")
        self._plataforma.dibujar("Confirmación", self._mensaje)

class NotificacionError(Notificacion):
    def mostrar(self) -> None:
        print("Mostrando notificación de error:")
        self._plataforma.dibujar("Error", self._mensaje)

