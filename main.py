from catalogo import CatalogoArte
from interfaz_usuario import *
from utilidades import *
# import threading

# def ejecutar_con_spinner(target_func, *args):
#     """Muestra un spinner mientras una función se ejecuta en segundo plano."""
#     spinner_chars = "|/-\\"
#     stop_spinner = threading.Event()

#     def spinner():
#         i = 0
#         while not stop_spinner.is_set():
#             print(f"\rCargando... {spinner_chars[i % len(spinner_chars)]}", end="", flush=True)
#             time.sleep(0.1)
#             i += 1
#         print("\r" + " " * 20 + "\r", end="") # Limpia la línea del spinner

#     spinner_thread = threading.Thread(target=spinner)
#     spinner_thread.start()
    
#     result = target_func(*args)
    
#     stop_spinner.set()
#     spinner_thread.join()
#     return result

def gestionar_busqueda_por_departamento(catalogo):
    """Gestiona el flujo de búsqueda de obras por departamento."""
    print("\nCargando departamentos...")
    departamentos = catalogo.obtener_departamentos()
    if not departamentos:
        mostrar_mensaje("No se pudieron cargar los departamentos.", es_error=True)
        input("Presione Enter para continuar...")
        return
    
    mostrar_departamentos(departamentos)
    id_dept = obtener_id_departamento()

    if id_dept == 'volver': return
    if id_dept is None:
        mostrar_mensaje("Debe ingresar un número de ID válido.", es_error=True)
        input("Presione Enter para continuar...")
        return
    
    print("\nBuscando obras...")
    obras = catalogo.buscar_por_departamento(id_dept)
    
    if obras is None:
        mostrar_mensaje(f"El ID de departamento '{id_dept}' no es válido.", es_error=True)
        input("Presione Enter para continuar...")
        return

    gestionar_resultados(catalogo, obras)

def gestionar_busqueda_por_nacionalidad(catalogo):
    """Gestiona el flujo de búsqueda de obras por nacionalidad del artista."""
    nacionalidades = catalogo.nacionalidades
    if not nacionalidades:
        mostrar_mensaje("La lista de nacionalidades no está disponible.", es_error=True)
        input("Presione Enter para continuar...")
        return
        
    mostrar_nacionalidades(nacionalidades)
    opcion = obtener_opcion_nacionalidad(len(nacionalidades))

    if opcion == 'volver': return
    if opcion is None:
        mostrar_mensaje("Selección no válida. Debe ingresar un número de la lista.", es_error=True)
        input("Presione Enter para continuar...")
        return
    
    nacionalidad_seleccionada = nacionalidades[opcion - 1]
    print(f"\nBuscando obras de artistas con nacionalidad '{nacionalidad_seleccionada}'...")
    obras = catalogo.buscar_por_nacionalidad(nacionalidad_seleccionada)
    gestionar_resultados(catalogo, obras)

def gestionar_busqueda_por_artista(catalogo):
    """Gestiona el flujo de búsqueda de obras por nombre del artista."""
    nombre_artista = obtener_nombre_artista()
    # if nombre_artista.lower() == 'q':
    #     animacion_despedida()
    #     sys.exit()
    if not nombre_artista.strip(): return
    
    print(f"\nBuscando obras de '{nombre_artista}'...")
    obras = catalogo.buscar_por_nombre_artista(nombre_artista)
    gestionar_resultados(catalogo, obras)

def gestionar_resultados(catalogo, obras):
    """Muestra una lista de resultados y permite al usuario ver detalles."""
    if not obras:
        mostrar_resumen_obras(obras)
        input("Presione Enter para continuar...")
        return

    while True:
        # limpiar_consola()
        mostrar_resumen_obras(obras)
        id_obra_str = obtener_id_obra()

        if not id_obra_str.strip():
            break
        
        obra_seleccionada = catalogo.obtener_obra_por_id(id_obra_str, obras)
        
        if obra_seleccionada:
            # limpiar_consola()
            mostrar_detalles_obra(obra_seleccionada)
            if preguntar_mostrar_imagen():
                mostrar_imagen(obra_seleccionada)
            input("\nPresione Enter para volver a la lista de obras...")
        else:
            mostrar_mensaje(f"El ID '{id_obra_str}' no es válido o no corresponde a ninguna obra en la lista.", es_error=True)
            input("Presione Enter para intentarlo de nuevo...")

def main():

    """====================================FUNCION DE BUCLE===================================="""
    
    # animacion_bienvenida()
    print("Iniciando Catálogo de Arte...")
    catalogo = CatalogoArte()
    
    while True:
        # limpiar_consola()
        mostrar_menu_principal()
        opcion = obtener_opcion_menu()

        if opcion == '1':
            gestionar_busqueda_por_departamento(catalogo)
        elif opcion == '2':
            gestionar_busqueda_por_nacionalidad(catalogo)
        elif opcion == '3':
            gestionar_busqueda_por_artista(catalogo)
        elif opcion == '4':
            break 
        else:
            mostrar_mensaje("Opción no válida. Por favor, intente de nuevo.", es_error=True)
            input("Presione Enter para continuar...")
    
    # animacion_despedida()
    print("\nGracias por su visita. ¡Hasta pronto!\n")

if __name__ == "__main__":
    main()