from catalogo import CatalogoArte
from interfaz_usuario import (
    mostrar_mensaje, mostrar_menu_principal, obtener_opcion_menu,
    mostrar_departamentos, obtener_id_departamento, mostrar_nacionalidades,
    obtener_opcion_nacionalidad, obtener_nombre_artista, mostrar_resumen_obras,
    obtener_id_obra, mostrar_detalles_obra, preguntar_mostrar_imagen
)
from utilidades import mostrar_imagen

def gestionar_busqueda_departamento(catalogo):
    departamentos = catalogo.obtener_departamentos()
    if not departamentos:
        mostrar_mensaje("No se pudieron cargar los departamentos.")
        return
    
    mostrar_departamentos(departamentos)
    id_dept = obtener_id_departamento()
    if id_dept is None:
        mostrar_mensaje("ID de departamento no válido.")
        return

    mostrar_mensaje(f"\nBuscando obras... Esto puede tardar un momento.")
    obras = catalogo.buscar_por_departamento(id_dept)
    gestionar_resultados(catalogo, obras)

def gestionar_busqueda_nacionalidad(catalogo):
    nacionalidades = catalogo.nacionalidades
    if not nacionalidades:
        mostrar_mensaje("La lista de nacionalidades no está disponible.")
        return
        
    mostrar_nacionalidades(nacionalidades)
    opcion = obtener_opcion_nacionalidad(len(nacionalidades))
    if opcion is None:
        mostrar_mensaje("Selección no válida.")
        return
    
    nacionalidad_seleccionada = nacionalidades[opcion - 1]
    mostrar_mensaje(f"\nBuscando obras de artistas con nacionalidad '{nacionalidad_seleccionada}'...")
    obras = catalogo.buscar_por_nacionalidad(nacionalidad_seleccionada)
    gestionar_resultados(catalogo, obras)

def gestionar_busqueda_artista(catalogo):
    nombre_artista = obtener_nombre_artista()
    if not nombre_artista:
        mostrar_mensaje("El nombre del artista no puede estar vacío.")
        return
    
    mostrar_mensaje(f"\nBuscando obras de '{nombre_artista}'...")
    obras = catalogo.buscar_por_nombre_artista(nombre_artista)
    gestionar_resultados(catalogo, obras)

def gestionar_resultados(catalogo, obras):
    mostrar_resumen_obras(obras)
    if not obras:
        return

    while True:
        id_obra = obtener_id_obra()
        if not id_obra:
            break
        
        obra = catalogo.obtener_obra_por_id(id_obra)
        if obra:
            mostrar_detalles_obra(obra)
            if preguntar_mostrar_imagen():
                mostrar_imagen(obra)
        else:
            mostrar_mensaje("ID de obra no encontrado en la lista actual.")

def main():
    catalogo = CatalogoArte()
    
    while True:
        mostrar_menu_principal()
        opcion = obtener_opcion_menu()

        if opcion == '1':
            gestionar_busqueda_departamento(catalogo)
        elif opcion == '2':
            gestionar_busqueda_nacionalidad(catalogo)
        elif opcion == '3':
            gestionar_busqueda_artista(catalogo)
        elif opcion == '4':
            mostrar_mensaje("Gracias por usar el catálogo. ¡Hasta pronto!")
            break
        else:
            mostrar_mensaje("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()