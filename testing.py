# API Documentation
# URL: https://metmuseum.github.io/
# https://drive.google.com/file/d/1tJEU6_VEeO6xFH8fssSfkw4M8MaN6U5A/view?usp=sharing

#EJEMPLO DE USO THREADING
import threading
import time

def simular_descarga(nombre_archivo, tiempo_espera):
    """
    Esta es la función que se ejecutará en un hilo separado.
    Simula una tarea que toma tiempo.
    """
    print(f"🟢 Iniciando la descarga del archivo: {nombre_archivo}...")
    time.sleep(tiempo_espera) # Simula el tiempo que tarda la descarga
    print(f"\n✅ ¡Descarga de '{nombre_archivo}' completada!")

# --- Programa Principal ---

print("▶️  Iniciando el programa principal.")

# 1. Crear el hilo (el "ayudante")
#    - target: es la función que queremos que el hilo ejecute.
#    - args: es una tupla con los argumentos que necesita esa función.
hilo_descarga = threading.Thread(target=simular_descarga, args=("documento_importante.pdf", 5))

# 2. Iniciar la ejecución del hilo
#    Esto pone a trabajar al "ayudante" en segundo plano.
hilo_descarga.start()

# 3. El programa principal continúa sin esperar
print("\nEl programa principal no está bloqueado. Puede hacer otras cosas mientras se descarga el archivo.")
for i in range(1, 4):
    print(f"Haciendo otra tarea en el hilo principal ({i}/3)...")
    time.sleep(1)

print("\n🏁 El programa principal ha terminado sus tareas, pero la descarga podría seguir.")

# Opcional: Si necesitas que el programa principal espere a que el hilo termine antes de continuar,
# puedes usar el método .join()
# hilo_descarga.join()
# print("Ahora sí, el programa confirma que la descarga ha finalizado por completo.")