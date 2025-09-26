from abc import ABC, abstractmethod
from typing import List


class ChatMediator(ABC):
    """
    Interfaz que define el contrato para el mediador del chat.
    El mediador centraliza la comunicación entre usuarios.
    """
    
    @abstractmethod
    def send_message(self, message: str, sender: 'User') -> None:
        """
        Envía un mensaje a todos los usuarios excepto al remitente.
        
        Args:
            message (str): El mensaje a enviar
            sender (User): El usuario que envía el mensaje
        """
        pass
    
    @abstractmethod
    def add_user(self, user: 'User') -> None:
        """
        Agrega un usuario al chat.
        
        Args:
            user (User): El usuario a agregar
        """
        pass
    
    @abstractmethod
    def remove_user(self, user: 'User') -> None:
        """
        Remueve un usuario del chat.
        
        Args:
            user (User): El usuario a remover
        """
        pass
