import collections
import random
import os

class MiCola:
    def __init__(self, desarrolladores):
        """Constructor: Inicializa la cola y muestra la bienvenida."""
        self.cola = collections.deque()
        self.desarrolladores = desarrolladores
        self.bienvenida()

    def bienvenida(self):
        print("="*50)
        print("      ¡BIENVENIDO AL PROGRAMA DE COLAS!")
        print(f" Desarrolladores: {self.desarrolladores}")
        print("="*50)

    def esta_vacia(self):
        return len(self.cola) == 0

    def agregar(self, elemento):
        self.cola.append(elemento)
        print(f"\n[+] Elemento '{elemento}' agregado con éxito.")

    def eliminar(self):
        if not self.esta_vacia():
            eliminado = self.cola.popleft()
            print(f"\n[-] Elemento '{eliminado}' eliminado del frente.")
            return eliminado
        print("\n[!] Error: La cola ya está vacía.")
        return None

    def mostrar_frente(self):
        if not self.esta_vacia():
            print(f"\n-> Primer elemento (Frente): {self.cola[0]}")
        else:
            print("\n[!] La cola está vacía.")

    def mostrar_final(self):
        if not self.esta_vacia():
            print(f"\n-> Último elemento (Final): {self.cola[-1]}")
        else:
            print("\n[!] La cola está vacía.")

    def mostrar_datos(self):
        if not self.esta_vacia():
            print(f"\nContenido de la cola: {list(self.cola)}")
        else:
            print("\n[!] La cola está vacía actualmente.")

    def contar_elementos(self):
        print(f"\nTotal de elementos en la cola: {len(self.cola)}")

    def copiar_cola(self):
        copia = list(self.cola)
        print(f"\nCopia generada: {copia}")
        return copia

    def encontrar_mayor(self):
        if not self.esta_vacia():
            print(f"\nEl número mayor en la cola es: {max(self.cola)}")
        else:
            print("\n[!] No hay elementos para comparar.")

    def mezclar_elementos(self):
        if not self.esta_vacia():
            lista_temp = list(self.cola)
            random.shuffle(lista_temp)
            self.cola = collections.deque(lista_temp)
            print("\n[~] Elementos mezclados aleatoriamente.")
        else:
            print("\n[!] No hay elementos para mezclar.")

    def __del__(self):
        """Destructor."""
        print("\n[Destructor] Recursos liberados. Saliendo del sistema...")

def menu():
    nombres = "Miguel Vega y Daniel Castaño"
    cola_obj = MiCola(nombres)
    
    while True:
        print("\n--- MENÚ DE OPERACIONES ---")
        print("1. Agregar elemento")
        print("2. Eliminar elemento")
        print("3. Mostrar primer elemento (Frente)")
        print("4. Mostrar último elemento (Final)")
        print("5. Mostrar todos los datos")
        print("6. Contar elementos")
        print("7. Encontrar el número mayor")
        print("8. Mezclar elementos")
        print("9. Copiar cola a una lista")
        print("10. Verificar si está vacía")
        print("0. Salir ")
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            dato = input("Ingrese el valor a agregar: ")
            cola_obj.agregar(dato)
        elif opcion == "2":
            cola_obj.eliminar()
        elif opcion == "3":
            cola_obj.mostrar_frente()
        elif opcion == "4":
            cola_obj.mostrar_final()
        elif opcion == "5":
            cola_obj.mostrar_datos()
        elif opcion == "6":
            cola_obj.contar_elementos()
        elif opcion == "7":
            cola_obj.encontrar_mayor()
        elif opcion == "8":
            cola_obj.mezclar_elementos()
        elif opcion == "9":
            cola_obj.copiar_cola()
        elif opcion == "10":
            if cola_obj.esta_vacia():
                print("\nLa cola está vacía.")
            else:
                print("\nLa cola NO está vacía.")
        elif opcion == "0":
            # Eliminamos el objeto manualmente para activar el destructor antes de cerrar
            del cola_obj
            print("Programa finalizado.")
            break
        else:
            print("\n[!] Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()