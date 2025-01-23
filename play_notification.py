import winsound
import os
import sys

def play_sound(filename: str, debug: bool = False) -> bool:
    """
    Reproduce un archivo de sonido WAV desde el directorio actual.
    
    Args:
        filename (str): Nombre del archivo WAV a reproducir
        debug (bool): Si es True, muestra información de diagnóstico
    
    Returns:
        bool: True si el sonido se reprodujo correctamente, False si hubo error
    """
    try:
        # Obtener la ruta absoluta del archivo
        current_dir = os.path.dirname(os.path.abspath(__file__))
        sound_file = os.path.join(current_dir, filename)
        
        if debug:
            print(f"Buscando en el directorio: {current_dir}")
            print("\nArchivos encontrados en el directorio:")
            for file in os.listdir(current_dir):
                print(f"- {file}")
            print(f"\nIntentando reproducir: {sound_file}")

        # Verificar si el archivo existe
        if not os.path.exists(sound_file):
            if debug:
                print(f"\nError: No se encuentra el archivo {sound_file}")
                wav_files = [f for f in os.listdir(current_dir) if f.endswith('.wav')]
                if wav_files:
                    print("\nArchivos WAV disponibles:")
                    for wav in wav_files:
                        print(f"- {wav}")
            return False

        # Reproducir el sonido
        winsound.PlaySound(sound_file, winsound.SND_FILENAME)
        return True

    except RuntimeError as e:
        if debug:
            print(f"Error reproduciendo el sonido: {e}")
        return False

# Ejemplo de uso
if __name__ == "__main__":
    # Reproducir con información de debug
    success = play_sound("send_messagges.wav", debug=True)
    if not success:
        print("No se pudo reproducir el sonido")
