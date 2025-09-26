from src.escenarios2_patron_bridge.plataformas import PlataformaEmail, PlataformaMovil, PlataformaWeb
from src.escenarios2_patron_bridge.notificaciones import NotificacionAlerta, NotificacionMensaje

if __name__ == "__main__":

    #Creacion de notificaciones con diferentes plataformas que vayamos utilizar en esta prueba
    plataforma_web = PlataformaWeb()
    plataforma_movil = PlataformaMovil()
    plataforma_email = PlataformaEmail()

    #Hacemos una prueba de un mensaje en la plataforma web
    notificacion_mensaje = NotificacionMensaje(
        plataforma_web, 
        "Recuerda reportar tus horas de trabajo antes del cierre de Q."
    )

    notificacion_mensaje.mostrar()

    #beneficio 4 - cambiamos la plataforma en tiempo de ejecución, para que el mensaje se muestre en otra plataforma si así lo deseamos
    #Cambiamos la plataforma a movil y mostramos el mismo mensaje
    notificacion_mensaje.set_plataforma(plataforma_movil)
    notificacion_mensaje.mostrar()

    #Cambiamos la plataforma a email y mostramos el mismo mensaje
    notificacion_mensaje.set_plataforma(plataforma_email)
    notificacion_mensaje.mostrar()

    #Hacemos una prueba de una alerta en la plataforma movil
    notificacion_alerta = NotificacionAlerta(
        plataforma_movil,
        "Se ha detectado actividad sospechosa en tu cuenta."
    )

    notificacion_alerta.mostrar()

    #Cambiamos la plataforma a email y mostramos el mismo mensaje
    notificacion_alerta.set_plataforma(plataforma_email)
    notificacion_alerta.mostrar()