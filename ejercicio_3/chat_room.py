from typing import List
from chat_mediator import ChatMediator
from user import User


class ChatRoom(ChatMediator):
    """
    Implementación concreta del mediador para el chat grupal.
    Centraliza la comunicación entre usuarios y gestiona la lista de participantes.
    """
    
    def __init__(self):
        """
        Inicializa una nueva sala de chat vacía.
        """
        self._users: List[User] = []
        self._room_name = "Sala Principal"
    
    def send_message(self, message: str, sender: User) -> None:
        """
        Envía un mensaje a todos los usuarios excepto al remitente.
        
        Args:
            message (str): El mensaje a enviar
            sender (User): El usuario que envía el mensaje
        """
        if sender not in self._users:
            print(f"⚠️  {sender.get_name()} no está en la sala de chat.")
            return
        
        print(f"📢 [{self._room_name}] {sender.get_name()}: {message}")
        
        # Enviar el mensaje a todos los usuarios excepto al remitente
        for user in self._users:
            if user != sender:
                user.receive(message, sender.get_name())
    
    def add_user(self, user: User) -> None:
        """
        Agrega un usuario a la sala de chat.
        
        Args:
            user (User): El usuario a agregar
        """
        if user not in self._users:
            self._users.append(user)
            user.set_mediator(self)
            print(f"✅ {user.get_name()} se ha unido a la sala de chat.")
            
            # Notificar a todos los usuarios sobre el nuevo miembro
            for other_user in self._users:
                if other_user != user:
                    other_user.receive(f"{user.get_name()} se ha unido al chat.", "Sistema")
        else:
            print(f"⚠️  {user.get_name()} ya está en la sala de chat.")
    
    def remove_user(self, user: User) -> None:
        """
        Remueve un usuario de la sala de chat.
        
        Args:
            user (User): El usuario a remover
        """
        if user in self._users:
            self._users.remove(user)
            print(f"👋 {user.get_name()} ha abandonado la sala de chat.")
            
            # Notificar a los usuarios restantes
            for other_user in self._users:
                other_user.receive(f"{user.get_name()} ha abandonado el chat.", "Sistema")
        else:
            print(f"⚠️  {user.get_name()} no está en la sala de chat.")
    
    def get_user_count(self) -> int:
        """
        Retorna el número de usuarios en la sala.
        
        Returns:
            int: Número de usuarios conectados
        """
        return len(self._users)
    
    def get_users(self) -> List[User]:
        """
        Retorna una copia de la lista de usuarios.
        
        Returns:
            List[User]: Lista de usuarios en la sala
        """
        return self._users.copy()
    
    def set_room_name(self, name: str) -> None:
        """
        Establece el nombre de la sala.
        
        Args:
            name (str): Nuevo nombre para la sala
        """
        self._room_name = name
        print(f"🏠 La sala ahora se llama: {name}")
    
    def get_room_name(self) -> str:
        """
        Retorna el nombre de la sala.
        
        Returns:
            str: Nombre de la sala
        """
        return self._room_name
