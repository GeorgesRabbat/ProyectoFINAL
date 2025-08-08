import requests
from modelos import Artista, ObraDeArte
class MetMuseumAPI:
    """Gestiona todas las comunicaciones con la API del Museo Metropolitano."""
    BASE_URL = "https://collectionapi.metmuseum.org/public/collection/v1"

    def obtener_departamentos(self):
        try:
            response = requests.get(f"{self.BASE_URL}/departments")
            response.raise_for_status()
            return response.json().get('departments', [])
        except requests.exceptions.RequestException as e:
            print(f"Error de conexión al obtener los departamentos: {e}")
            return None

    def buscar_objetos(self, consulta):
        try:
            response = requests.get(f"{self.BASE_URL}/search?q={consulta}")
            response.raise_for_status()
            return response.json().get('objectIDs', [])
        except requests.exceptions.RequestException as e:
            print(f"Error de conexión durante la búsqueda de '{consulta}': {e}")
            return []

    def obtener_detalles_obra(self, id_objeto):
        try:
            response = requests.get(f"{self.BASE_URL}/objects/{id_objeto}")
            response.raise_for_status()
            data = response.json()
            artista = Artista(
                nombre=data.get('artistDisplayName', 'Desconocido'),
                nacionalidad=data.get('artistNationality', 'Desconocida'),
                fecha_nacimiento=data.get('artistBeginDate', 'N/A'),
                fecha_muerte=data.get('artistEndDate', 'N/A')
            )
            obra = ObraDeArte(
                id_objeto=data.get('objectID'),
                titulo=data.get('title', 'Sin título'),
                clasificacion=data.get('classification', 'No clasificado'),
                fecha_objeto=data.get('objectDate', 'Fecha desconocida'),
                artista=artista,
                url_imagen=data.get('primaryImageSmall')
            )
            return obra
        except requests.exceptions.RequestException:
            return None