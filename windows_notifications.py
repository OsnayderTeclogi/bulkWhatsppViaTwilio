from plyer import notification

def show_windows_notification(title="Notificación", message="", duration=10, icon_path=None):
    """
    Muestra una notificación en Windows
    
    Args:
        title (str): Título de la notificación
        message (str): Mensaje de la notificación
        duration (int): Duración en segundos
        icon_path (str): Ruta al ícono (opcional)
    """
    try:
        notification.notify(
            title=title,
            message=message,
            app_icon=icon_path,
            timeout=duration,
            app_name="Python Script"
        )
    except Exception as e:
        print(f"Error mostrando notificación: {str(e)}")
