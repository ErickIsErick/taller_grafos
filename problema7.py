from collections import defaultdict


class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.grafo = defaultdict(list)

    def agregar_arista(self, origen, destino):
        self.grafo[origen].append(destino)
        self.grafo[destino].append(origen)

    def mostrar_grafo(self):
        print("\nGrafo representado con listas de adyacencia:")
        for nodo, vecinos in self.grafo.items():
            print(f"  {nodo} -> {', '.join(map(str, vecinos))}")

    def encontrar_caminos_hamiltonianos(self):
        def backtrack(nodo, visitados, camino):
            visitados.add(nodo)
            camino.append(nodo)

            if len(camino) == self.num_vertices:
                caminos_hamiltonianos.append(camino[:])
            else:

                for vecino in self.grafo[nodo]:
                    if vecino not in visitados:
                        backtrack(vecino, visitados, camino)

            camino.pop()
            visitados.remove(nodo)

        caminos_hamiltonianos = []
        for inicio in range(self.num_vertices):
            backtrack(inicio, set(), [])

        return caminos_hamiltonianos

# Construir el grafo
def construir_grafo():
    num_vertices = 4  # Número de vértices
    grafo = Grafo(num_vertices)

    # Aristas del grafo
    arcos = [
        (0, 1), (0, 2), (1, 2),
        (1, 3), (2, 3)
    ]

    for origen, destino in arcos:
        grafo.agregar_arista(origen, destino)

    return grafo

if __name__ == "__main__":
    print("=== Caminos Hamiltonianos en un Grafo ===")

    # 
    grafo = construir_grafo()

    
    grafo.mostrar_grafo()
 
    caminos = grafo.encontrar_caminos_hamiltonianos()
    if caminos:
        print("\nCaminos Hamiltonianos encontrados:")
        for camino in caminos:
            print(" -> ".join(map(str, camino)))
    else:
        print("\nNo se encontraron caminos Hamiltonianos.")
