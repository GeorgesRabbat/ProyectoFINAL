import requests
from PIL import Image

def guardar_imagen_desde_url(url, nombre_archivo):
    """
    Descarga una imagen desde una URL y la guarda en un archivo local.

    Args:
        url (str): La URL de la imagen a descargar.
        nombre_archivo (str): El nombre base para el archivo (sin extensión).

    Returns:
        str: La ruta completa al archivo guardado si tiene éxito, de lo contrario None.
    """
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        content_type = response.headers.get('Content-Type')
        extension = '.jpg'
        if content_type:
            if 'image/png' in content_type:
                extension = '.png'
            elif 'image/jpeg' in content_type:
                extension = '.jpg'
            elif 'image/svg+xml' in content_type:
                extension = '.svg'
        
        nombre_archivo_final = f"{nombre_archivo}{extension}"

        with open(nombre_archivo_final, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        
        print(f"Imagen guardada exitosamente como '{nombre_archivo_final}'")
        return nombre_archivo_final

    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la petición a la URL: {e}")
        return None
    except IOError as e:
        print(f"Error al escribir el archivo en el disco: {e}")
        return None

api_url = "https://images.metmuseum.org/CRDImages/ep/original/DT1567.jpg"
nombre_archivo_destino = "logo_aleatorio"

ruta_final = guardar_imagen_desde_url(api_url, nombre_archivo_destino)

if ruta_final:
    try:
        img = Image.open(ruta_final)
        img.show()
    except Exception as e:
        print(f"No se pudo abrir la imagen. Error: {e}")