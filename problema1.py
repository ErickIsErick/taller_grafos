from collections import defaultdict, deque


class Grafo:
    def __init__(self):
        self.grafo = defaultdict(list)

    def agregar_arista(self, origen, destino, peso):
        self.grafo[origen].append((destino, peso))

    def mostrar_grafo(self):
        print("\nGrafo representado con listas de adyacencia:")
        for nodo, vecinos in self.grafo.items():
            print(f"  {nodo} -> {', '.join([f'{v} (peso {p})' for v, p in vecinos])}")

    def bfs(self, inicio):
        print(f"\nRecorrido en anchura (BFS) desde el vértice {inicio}:")
        visitados = set()
        cola = deque([inicio])
        resultado = []

        while cola:
            nodo = cola.popleft()
            if nodo not in visitados:
                visitados.add(nodo)
                resultado.append(nodo)
                for vecino, _ in self.grafo[nodo]:
                    if vecino not in visitados:
                        cola.append(vecino)

        print(" -> ".join(map(str, resultado)))


def construir_grafo():
    vertices = [4, 7, 14, 19, 21, 25]
    grafo = Grafo()

    for i in range(len(vertices)):
        for j in range(i):
            peso = vertices[i] - vertices[j]
            grafo.agregar_arista(vertices[i], vertices[j], peso)

    return grafo

if __name__ == "__main__":
    print("=== Representación y Recorrido de un Grafo Valorado ===")
    
    grafo = construir_grafo()
    grafo.mostrar_grafo()


    while True:
        try:
            inicio = int(input("\nIngrese el vértice desde donde realizar el BFS: "))
            if inicio not in grafo.grafo:
                print("El vértice ingresado no está en el grafo. Intente nuevamente.")
                continue
            break
        except ValueError:
            print("Entrada no válida. Ingrese un número entero.")

    grafo.bfs(inicio)
