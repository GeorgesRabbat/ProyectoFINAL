def mostrar_mensaje(mensaje):
    print(mensaje)

def mostrar_menu_principal():
    print("\n--- Catálogo de Arte del Museo Metropolitano ---")
    print("1. Ver lista de obras por Departamento")
    print("2. Ver lista de obras por Nacionalidad del autor")
    print("3. Ver lista de obras por Nombre del autor")
    print("4. Salir")
    print("------------------------------------------------")

def obtener_opcion_menu():
    return input("Seleccione una opción: ")

def mostrar_departamentos(departamentos):
    print("\n--- Departamentos del Museo ---")
    for dept in departamentos:
        print(f"ID: {dept['departmentId']}, Nombre: {dept['displayName']}")
    print("-----------------------------\n")

def obtener_id_departamento():
    try:
        return int(input("Ingrese el ID del departamento que desea consultar: "))
    except ValueError:
        return None

def mostrar_nacionalidades(nacionalidades):
    print("\n--- Nacionalidades Disponibles ---")
    for i, nat in enumerate(nacionalidades, 1):
        print(f"{i}. {nat}")
    print("----------------------------------\n")

def obtener_opcion_nacionalidad(max_opcion):
    try:
        opcion = int(input("Seleccione el número de la nacionalidad: "))
        if 1 <= opcion <= max_opcion:
            return opcion
        return None
    except ValueError:
        return None

def obtener_nombre_artista():
    return input("Ingrese el nombre del autor a buscar: ")

def mostrar_resumen_obras(obras):
    if not obras:
        print("No se encontraron obras que coincidan con los criterios.")
        return
    print("\n--- Obras Encontradas ---")
    for obra in obras:
        print(f"  - ID: {obra.id_objeto}, Título: {obra.titulo}, Artista: {obra.artista.nombre}")
    print("-------------------------\n")

def obtener_id_obra():
    return input("Ingrese el ID de la obra para ver sus detalles (o presione Enter para volver): ")

def mostrar_detalles_obra(obra):
    print("\n--- Detalles de la Obra ---")
    print(f"Título: {obra.titulo}")
    print(f"Artista: {obra.artista.nombre}")
    print(f"Nacionalidad: {obra.artista.nacionalidad}")
    print(f"Periodo de vida: {obra.artista.fecha_nacimiento} - {obra.artista.fecha_muerte}")
    print(f"Tipo/Clasificación: {obra.clasificacion}")
    print(f"Año de Creación: {obra.fecha_objeto}")
    print("---------------------------\n")

def preguntar_mostrar_imagen():
    opcion = input("¿Desea ver la imagen de esta obra? (s/n): ").lower()
    return opcion == 's'