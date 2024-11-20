from collections import defaultdict, deque

# Clase para representar el grafo dirigido
class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.grafo = defaultdict(list)
        self.entradas = [0] * num_vertices  

    def agregar_arco(self, origen, destino):
        self.grafo[origen].append(destino)
        self.entradas[destino] += 1

    def mostrar_grafo(self):
        print("\nGrafo representado con listas de adyacencia:")
        for nodo, sucesores in self.grafo.items():
            print(f"  {nodo} -> {', '.join(map(str, sucesores))}")

    def tiene_ciclos(self):
        cola = deque([nodo for nodo in range(self.num_vertices) if self.entradas[nodo] == 0])
        eliminados = 0 

        while cola:
            nodo = cola.popleft()
            eliminados += 1


            for sucesor in self.grafo[nodo]:
                self.entradas[sucesor] -= 1
                if self.entradas[sucesor] == 0: 
                    cola.append(sucesor)

        return eliminados != self.num_vertices


def construir_grafo_desde_entrada():
    print("\n=== Construcción del Grafo Dirigido ===")
    print("Por favor, siga las instrucciones para ingresar los datos del grafo.")

    while True:
        try:
            num_vertices = int(input("Ingrese el número total de vértices (nodos) en el grafo: "))
            if num_vertices <= 0:
                print("El número de vértices debe ser mayor a 0. Intente nuevamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

    grafo = Grafo(num_vertices)

    # Solicitar las aristas
    print("\nIngrese las aristas en el formato 'origen destino' (por ejemplo, '0 1').")
    print("Cuando termine de ingresar todas las aristas, escriba 'fin' para finalizar.")
    while True:
        entrada = input("Arista (origen destino): ")
        if entrada.strip().lower() == "fin":
            break
        try:
            origen, destino = map(int, entrada.split())
            if origen < 0 or origen >= num_vertices or destino < 0 or destino >= num_vertices:
                print(f"Los vértices deben estar entre 0 y {num_vertices - 1}. Intente nuevamente.")
                continue
            grafo.agregar_arco(origen, destino)
        except ValueError:
            print("Formato inválido. Por favor, ingrese dos números enteros separados por un espacio.")

    return grafo


# Main
if __name__ == "__main__":
    print("\n=== Verificar Ciclos en un Grafo Dirigido ===")
    print("Este programa determinará si el grafo contiene ciclos.")
    print("Debe ingresar las aristas de forma clara y completa.\n")

    grafo = construir_grafo_desde_entrada()

    grafo.mostrar_grafo()

    if grafo.tiene_ciclos():
        print("\nEl grafo contiene ciclos.")
    else:
        print("\nEl grafo NO contiene ciclos.")
