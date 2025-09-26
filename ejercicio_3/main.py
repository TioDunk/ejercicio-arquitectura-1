"""
Ejemplo de uso del patrón Mediator para un chat grupal.

Este ejemplo demuestra cómo el patrón Mediator centraliza la comunicación
entre usuarios, evitando que cada usuario tenga que conocer directamente
a todos los demás.
"""

from chat_room import ChatRoom
from concrete_user import ConcreteUser


def main():
    """
    Función principal que demuestra el uso del patrón Mediator.
    """
    print("🚀 Iniciando ejemplo del patrón Mediator - Chat Grupal")
    print("=" * 60)
    
    # Crear la sala de chat (mediador)
    chat_room = ChatRoom()
    chat_room.set_room_name("Sala de Desarrollo")
    
    print(f"\n🏠 Sala creada: {chat_room.get_room_name()}")
    print(f"👥 Usuarios conectados: {chat_room.get_user_count()}")
    
    # Crear usuarios
    print("\n👤 Creando usuarios...")
    alice = ConcreteUser("Alice")
    bob = ConcreteUser("Bob")
    charlie = ConcreteUser("Charlie")
    diana = ConcreteUser("Diana")
    
    # Agregar usuarios a la sala
    print("\n➕ Agregando usuarios a la sala...")
    chat_room.add_user(alice)
    chat_room.add_user(bob)
    chat_room.add_user(charlie)
    chat_room.add_user(diana)
    
    print(f"👥 Usuarios conectados: {chat_room.get_user_count()}")
    
    # Simular conversación
    print("\n💬 Iniciando conversación...")
    print("-" * 40)
    
    alice.send("¡Hola a todos! ¿Cómo están?")
    bob.send("¡Hola Alice! Todo bien, gracias.")
    charlie.send("¡Hola! ¿Alguien más está trabajando en el proyecto?")
    diana.send("Sí, yo estoy trabajando en la interfaz de usuario.")
    alice.send("Perfecto, yo estoy con la lógica de negocio.")
    bob.send("Yo me encargo de las pruebas unitarias.")
    
    print("-" * 40)
    
    # Demostrar que los usuarios no necesitan conocer a otros usuarios directamente
    print("\n🔍 Demostrando desacoplamiento...")
    print(f"Alice conoce a Bob directamente: {hasattr(alice, '_users')}")
    print(f"Alice usa el mediador: {alice.get_mediator() is not None}")
    
    # Mostrar historial de mensajes de Alice
    print(f"\n📚 Historial de mensajes de Alice:")
    for msg in alice.get_message_history():
        status = "📤" if msg.get('sent', False) else "📥"
        print(f"  {status} [{msg['timestamp']}] {msg['sender']}: {msg['message']}")
    
    # Simular entrada y salida de usuarios
    print("\n🔄 Simulando entrada y salida de usuarios...")
    eve = ConcreteUser("Eve")
    chat_room.add_user(eve)
    
    eve.send("¡Hola! Soy nueva en el equipo.")
    alice.send("¡Bienvenida Eve!")
    
    # Diana se va
    print("\n👋 Diana se desconecta...")
    diana.disconnect()
    
    charlie.send("¿Diana se fue?")
    alice.send("Sí, se desconectó.")
    
    # Mostrar estadísticas finales
    print(f"\n📊 Estadísticas finales:")
    print(f"  👥 Usuarios en sala: {chat_room.get_user_count()}")
    print(f"  📨 Mensajes de Alice: {len(alice.get_sent_messages())} enviados, {len(alice.get_received_messages())} recibidos")
    print(f"  📨 Mensajes de Bob: {len(bob.get_sent_messages())} enviados, {len(bob.get_received_messages())} recibidos")
    
    # Demostrar beneficios del patrón
    print(f"\n✅ Beneficios del patrón Mediator demostrados:")
    print(f"  1. ✅ Fácil mantenimiento: Agregar/remover usuarios sin modificar otros")
    print(f"  2. ✅ Organización centralizada: Toda la lógica de comunicación en ChatRoom")
    print(f"  3. ✅ Reducción de complejidad: Sin dependencias directas entre usuarios")
    
    print(f"\n🎯 Los usuarios solo conocen al mediador, no entre sí:")
    for user in [alice, bob, charlie, eve]:
        print(f"  {user.get_name()}: Mediador = {type(user.get_mediator()).__name__}")


def demo_escalabilidad():
    """
    Demuestra la escalabilidad del patrón Mediator.
    """
    print("\n" + "=" * 60)
    print("🚀 DEMO DE ESCALABILIDAD")
    print("=" * 60)
    
    # Crear una sala más grande
    sala_grande = ChatRoom()
    sala_grande.set_room_name("Sala de Conferencia")
    
    # Crear muchos usuarios
    usuarios = []
    for i in range(10):
        usuario = ConcreteUser(f"Usuario{i+1}")
        sala_grande.add_user(usuario)
        usuarios.append(usuario)
    
    print(f"👥 Sala grande creada con {sala_grande.get_user_count()} usuarios")
    
    # Simular mensajes masivos
    print("\n💬 Simulando mensajes masivos...")
    for i, usuario in enumerate(usuarios[:5]):  # Solo los primeros 5 envían
        usuario.send(f"Mensaje de prueba #{i+1}")
    
    print(f"✅ {sala_grande.get_user_count()} usuarios manejados eficientemente")
    print("✅ Sin dependencias directas entre usuarios")
    print("✅ Fácil agregar/remover usuarios dinámicamente")


if __name__ == "__main__":
    main()
    demo_escalabilidad()
    
    print("\n" + "=" * 60)
    print("🎉 Ejemplo completado exitosamente!")
    print("El patrón Mediator ha centralizado la comunicación del chat grupal.")
    print("=" * 60)
