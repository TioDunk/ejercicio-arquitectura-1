from abc import ABC, abstractmethod
from typing import Optional
from chat_mediator import ChatMediator


class User(ABC):
    """
    Clase abstracta que representa un usuario del chat.
    Define la interfaz común para todos los usuarios y maneja la comunicación
    a través del mediador.
    """
    
    def __init__(self, name: str):
        """
        Inicializa un usuario con un nombre.
        
        Args:
            name (str): Nombre del usuario
        """
        self._name = name
        self._mediator: Optional[ChatMediator] = None
    
    def send(self, message: str) -> None:
        """
        Envía un mensaje a través del mediador.
        
        Args:
            message (str): El mensaje a enviar
        """
        if self._mediator is None:
            print(f"⚠️  {self._name} no está conectado a ninguna sala de chat.")
            return
        
        self._mediator.send_message(message, self)
    
    @abstractmethod
    def receive(self, message: str, sender_name: str) -> None:
        """
        Recibe un mensaje de otro usuario.
        
        Args:
            message (str): El mensaje recibido
            sender_name (str): Nombre del usuario que envió el mensaje
        """
        pass
    
    def get_name(self) -> str:
        """
        Retorna el nombre del usuario.
        
        Returns:
            str: Nombre del usuario
        """
        return self._name
    
    def set_mediator(self, mediator: ChatMediator) -> None:
        """
        Establece el mediador para este usuario.
        
        Args:
            mediator (ChatMediator): El mediador a usar
        """
        self._mediator = mediator
    
    def get_mediator(self) -> Optional[ChatMediator]:
        """
        Retorna el mediador actual.
        
        Returns:
            Optional[ChatMediator]: El mediador actual o None
        """
        return self._mediator
    
    def disconnect(self) -> None:
        """
        Desconecta al usuario del mediador.
        """
        if self._mediator is not None:
            self._mediator.remove_user(self)
            self._mediator = None
