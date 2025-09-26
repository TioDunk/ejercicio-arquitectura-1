from user import User


class ConcreteUser(User):
    """
    Implementación concreta de un usuario del chat.
    Representa un usuario real que puede enviar y recibir mensajes.
    """
    
    def __init__(self, name: str):
        """
        Inicializa un usuario concreto.
        
        Args:
            name (str): Nombre del usuario
        """
        super().__init__(name)
        self._message_history = []
    
    def receive(self, message: str, sender_name: str) -> None:
        """
        Recibe un mensaje de otro usuario y lo almacena en el historial.
        
        Args:
            message (str): El mensaje recibido
            sender_name (str): Nombre del usuario que envió el mensaje
        """
        # Almacenar el mensaje en el historial
        self._message_history.append({
            'sender': sender_name,
            'message': message,
            'timestamp': self._get_timestamp()
        })
        
        # Mostrar el mensaje recibido
        print(f"📨 {self._name} recibió de {sender_name}: {message}")
    
    def send(self, message: str) -> None:
        """
        Envía un mensaje a través del mediador.
        
        Args:
            message (str): El mensaje a enviar
        """
        # Almacenar el mensaje enviado en el historial
        self._message_history.append({
            'sender': self._name,
            'message': message,
            'timestamp': self._get_timestamp(),
            'sent': True
        })
        
        # Enviar a través del mediador
        super().send(message)
    
    def get_message_history(self) -> list:
        """
        Retorna el historial de mensajes del usuario.
        
        Returns:
            list: Lista de mensajes con información de timestamp
        """
        return self._message_history.copy()
    
    def get_received_messages(self) -> list:
        """
        Retorna solo los mensajes recibidos.
        
        Returns:
            list: Lista de mensajes recibidos
        """
        return [msg for msg in self._message_history if not msg.get('sent', False)]
    
    def get_sent_messages(self) -> list:
        """
        Retorna solo los mensajes enviados.
        
        Returns:
            list: Lista de mensajes enviados
        """
        return [msg for msg in self._message_history if msg.get('sent', False)]
    
    def clear_history(self) -> None:
        """
        Limpia el historial de mensajes del usuario.
        """
        self._message_history.clear()
        print(f"🗑️  {self._name} ha limpiado su historial de mensajes.")
    
    def _get_timestamp(self) -> str:
        """
        Genera un timestamp simple para los mensajes.
        
        Returns:
            str: Timestamp en formato HH:MM:SS
        """
        from datetime import datetime
        return datetime.now().strftime("%H:%M:%S")
    
    def get_status(self) -> str:
        """
        Retorna el estado del usuario.
        
        Returns:
            str: Estado del usuario
        """
        if self._mediator is None:
            return "Desconectado"
        else:
            return "Conectado"
    
    def __str__(self) -> str:
        """
        Representación en string del usuario.
        
        Returns:
            str: Información del usuario
        """
        return f"Usuario: {self._name} ({self.get_status()})"
    
    def __repr__(self) -> str:
        """
        Representación técnica del usuario.
        
        Returns:
            str: Representación técnica
        """
        return f"ConcreteUser(name='{self._name}', status='{self.get_status()}')"
