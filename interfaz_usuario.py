def mostrar_mensaje(mensaje, es_error=False):
    prefijo = "ERROR: " if es_error else ""
    print(f"\n{prefijo}{mensaje}")

def mostrar_menu_principal():
    print("\n--- Catálogo de Arte del Museo Metropolitano ---")
    print("1. Buscar obras por Departamento")
    print("2. Buscar obras por Nacionalidad del autor")
    print("3. Buscar obras por Nombre del autor")
    print("4. Salir")
    print("------------------------------------------------")

def obtener_opcion_menu():
    return input("Seleccione una opción: ")

def mostrar_departamentos(departamentos):
    #Seleccion de volver con enter
    print("\n--- Departamentos del Museo (Presione Enter para regresar) ---")
    if departamentos:
        for dept in departamentos:
            print(f"ID: {dept['departmentId']:<5} Nombre: {dept['displayName']}")
    print("-----------------------------------------------------------------")

def obtener_id_departamento():
    entrada = input("Ingrese el ID del departamento que desea consultar: ")
    if not entrada.strip():
        return 'volver'
    try:
        return int(entrada)
    except ValueError:
        return None

def mostrar_nacionalidades(nacionalidades):
    #Seleccion de volver con enter
    print("\n--- Nacionalidades (Presione Enter para regresar) ---")
    if nacionalidades:
        for i, nat in enumerate(nacionalidades, 1):
            print(f"{i}. {nat}")
    print("-------------------------------------------------------")

def obtener_opcion_nacionalidad(max_opcion):
    entrada = input("Seleccione el número de la nacionalidad: ")
    #Revisa que el valor de entrada no este vacio
    if not entrada.strip():
        return 'volver'
    try:
        opcion = int(entrada)
        if 1 <= opcion <= max_opcion:
            return opcion
        return None
    except ValueError:
        return None

def obtener_nombre_artista():
    #se actualiza el texto para indicar que se puede presionar Enter.
    return input("Ingrese el nombre del autor (o presione Enter para regresar): ")

def mostrar_resumen_obras(obras):
    if not obras:
        print("\nNo se encontraron obras que coincidan con los criterios.")
        return
    print("\n--- Obras Encontradas ---")
    for obra in obras:
        print(f"  - ID: {obra.id_objeto:<10} Título: {obra.titulo:<50} Artista: {obra.artista.nombre}")
    print("-------------------------\n")

def obtener_id_obra():
    #Se actualiza el texto para indicar que se puede volver con enter
    return input("Ingrese el ID de una obra para ver sus detalles (o presione Enter para volver): ")

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