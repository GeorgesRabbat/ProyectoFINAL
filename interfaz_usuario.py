# import sys
# from utilidades import animacion_despedida

def mostrar_mensaje(mensaje, es_error=False):
    """Muestra un mensaje formateado al usuario."""
    prefijo = ">> ERROR:" if es_error else ">>"
    print(f"\n{prefijo} {mensaje}")

def mostrar_menu_principal():
    """Imprime el menú principal de opciones."""
    print("\n--- Catálogo de Arte del Museo Metropolitano ---")
    print("1. Buscar obras por Departamento")
    print("2. Buscar obras por Nacionalidad del autor")
    print("3. Buscar obras por Nombre del autor")
    print("\n4. Salir del programa")
    print("------------------------------------------------")

def obtener_opcion_menu():
    """Solicita al usuario que elija una opción del menú."""
    return input("Seleccione una opción: ")

def mostrar_departamentos(departamentos):
    """Muestra una lista de departamentos con sus IDs."""
    print("\n--- Departamentos (Enter para volver) ---")
    if departamentos:
        for dept in departamentos:
            print(f"ID: {dept['departmentId']:<5} Nombre: {dept['displayName']}")
    print("-----------------------------------------------------------------")

def obtener_id_departamento():
    """Solicita al usuario el ID de un departamento."""
    entrada = input("Ingrese el ID del departamento: ")
    # if entrada.lower() == 'q':
    #     animacion_despedida()
    #     sys.exit()
    if not entrada.strip():
        return 'volver'
    try:
        return int(entrada)
    except ValueError:
        return None

def mostrar_nacionalidades(nacionalidades):
    """Muestra una lista numerada de nacionalidades."""
    print("\n--- Nacionalidades (Enter para volver) ---")
    if nacionalidades:
        for i, nat in enumerate(nacionalidades, 1):
            print(f"{i}. {nat}")
    print("-------------------------------------------------------")

def obtener_opcion_nacionalidad(max_opcion):
    """Solicita al usuario que elija una nacionalidad de la lista."""
    entrada = input("Seleccione el número de la nacionalidad: ")
    # if entrada.lower() == 'q':
    #     animacion_despedida()
    #     sys.exit()
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
    """Solicita al usuario el nombre de un artista."""
    return input("Ingrese el nombre del autor (Enter para volver | 'q' para salir): ")

def mostrar_resumen_obras(obras):
    """Muestra un resumen de una lista de obras."""
    if not obras:
        print("\nNo se encontraron obras que coincidan con los criterios.")
        return
    print("\n--- Obras Encontradas ---")
    for obra in obras:
        print(f"  - ID: {obra.id_objeto:<10} Título: {obra.titulo:<50} Artista: {obra.artista.nombre}")
    print("-------------------------\n")

def obtener_id_obra():
    """Solicita al usuario el ID de una obra para ver sus detalles."""
    return input("Ingrese el ID de una obra para ver sus detalles (Enter para volver): ")

def mostrar_detalles_obra(obra):
    """Muestra todos los detalles de una obra."""
    print("\n--- Detalles de la Obra ---")
    print(f"Título: {obra.titulo}")
    print(f"Artista: {obra.artista.nombre}")
    print(f"Nacionalidad: {obra.artista.nacionalidad}")
    print(f"Periodo de vida: {obra.artista.fecha_nacimiento} - {obra.artista.fecha_muerte}")
    print(f"Tipo/Clasificación: {obra.clasificacion}")
    print(f"Año de Creación: {obra.fecha_objeto}")
    print("---------------------------\n")

def preguntar_mostrar_imagen():
    """Pregunta al usuario si desea ver la imagen de la obra."""
    opcion = input("¿Desea ver la imagen de esta obra? (s/n): ").lower()
    return opcion == 's'
