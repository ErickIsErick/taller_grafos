from collections import defaultdict


class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.grafo = defaultdict(list)  

    def agregar_arco(self, origen, destino, peso):
        self.grafo[origen].append((destino, peso))

    def mostrar_grafo(self):
        print("\nGrafo representado con listas de adyacencia:")
        for nodo, vecinos in self.grafo.items():
            print(f"  {nodo} -> {', '.join([f'{v} (peso: {p})' for v, p in vecinos])}")

    def convertir_a_matriz(self):

        matriz = [[0] * self.num_vertices for _ in range(self.num_vertices)]

        for origen, vecinos in self.grafo.items():
            for destino, peso in vecinos:
                matriz[origen][destino] = peso

        return matriz

    def mostrar_matriz(self, matriz):
        print("\nMatriz de pesos:")
        for fila in matriz:
            print("  ".join(map(str, fila)))


def construir_grafo():
    num_vertices = 5 
    grafo = Grafo(num_vertices)


    arcos = [
        (0, 1, 10), (0, 2, 5), (1, 2, 3),
        (2, 3, 8), (3, 4, 2), (4, 0, 7)
    ]

    for origen, destino, peso in arcos:
        grafo.agregar_arco(origen, destino, peso)

    return grafo

if __name__ == "__main__":
    print("=== Grafo: Listas de Adyacencia a Matriz de Pesos ===")
    
    grafo = construir_grafo()
    grafo.mostrar_grafo()

    matriz = grafo.convertir_a_matriz()


    grafo.mostrar_matriz(matriz)
