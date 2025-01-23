from windows_notifications import show_windows_notification

# ...existing code...

# Al final de tu script principal
if __name__ == "__main__":
    try:
        # ...existing code...
        show_windows_notification(
            title="Script Finalizado",
            message="La ejecución del script ha terminado correctamente"
        )
    except Exception as e:
        show_windows_notification(
            title="Error en el Script",
            message=f"Ha ocurrido un error: {str(e)}"
        )
