from cliente_api import MetMuseumAPI
from utilidades import cargar_nacionalidades

class CatalogoArte:
    def __init__(self):
        self.api = MetMuseumAPI()
        self.nacionalidades = cargar_nacionalidades()
        self.cache_obras = {}

    def _obtener_detalles_obra(self, id_objeto):
        if id_objeto in self.cache_obras:
            return self.cache_obras[id_objeto]
        
        obra = self.api.obtener_detalles_obra(id_objeto)
        if obra:
            self.cache_obras[id_objeto] = obra
        return obra

    def obtener_departamentos(self):
        return self.api.obtener_departamentos()

    def buscar_por_departamento(self, id_departamento):
        departamentos = self.obtener_departamentos()
        nombre_dept = ""
        for dept in departamentos:
            if dept['departmentId'] == id_departamento:
                nombre_dept = dept['displayName']
                break
        
        if not nombre_dept:
            return []

        ids_objetos = self.api.buscar_objetos(nombre_dept)
        obras = [self._obtener_detalles_obra(obj_id) for obj_id in ids_objetos[:20] if obj_id]
        return [obra for obra in obras if obra is not None]

    def buscar_por_nacionalidad(self, nacionalidad):
        ids_objetos = self.api.buscar_objetos(nacionalidad)
        obras = []
        for obj_id in ids_objetos[:50]:
            obra = self._obtener_detalles_obra(obj_id)
            if obra and obra.artista.nacionalidad.lower() == nacionalidad.lower():
                obras.append(obra)
            if len(obras) >= 20:
                break
        return obras
        
    def buscar_por_nombre_artista(self, nombre_artista):
        ids_objetos = self.api.buscar_objetos(nombre_artista)
        obras = []
        for obj_id in ids_objetos[:50]:
            obra = self._obtener_detalles_obra(obj_id)
            if obra and nombre_artista.lower() in obra.artista.nombre.lower():
                obras.append(obra)
            if len(obras) >= 20:
                break
        return obras
        
    def obtener_obra_por_id(self, id_obra):
        try:
            return self._obtener_detalles_obra(int(id_obra))
        except (ValueError, TypeError):
            return None