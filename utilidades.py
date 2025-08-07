import requests
from PIL import Image
from io import BytesIO
from modelos import ObraDeArte

def cargar_nacionalidades():
    url = "https://drive.google.com/uc?export=download&id=1tJEU6_VEeO6xFH8fssSfkw4M8MaN6U5A"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return [line.strip() for line in response.content.decode('utf-8').splitlines() if line.strip()]
    except requests.exceptions.RequestException as e:
        print(f"Error crítico: no se pudo cargar la lista de nacionalidades. {e}")
        return []

def mostrar_imagen(obra):
    if not obra.url_imagen:
        print("Lo sentimos, esta obra no tiene una imagen disponible.")
        return
    try:
        print(f"Cargando imagen para '{obra.titulo}'...")
        response = requests.get(obra.url_imagen)
        response.raise_for_status()
        imagen = Image.open(BytesIO(response.content))
        imagen.show(title=obra.titulo)
    except requests.exceptions.RequestException as e:
        print(f"Error al descargar la imagen: {e}")
    except Exception as e:
        print(f"No se pudo mostrar la imagen. Error: {e}")