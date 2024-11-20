import heapq
from collections import defaultdict

class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.grafo = defaultdict(list)

    def agregar_arista(self, origen, destino, peso):
        self.grafo[origen].append((destino, peso))

    def dijkstra_invertido(self, destino):
        distancias = [float('inf')] * self.num_vertices
        distancias[destino] = 0

        cola_prioridad = [(0, destino)]  # (distancia, nodo)
        while cola_prioridad:
            distancia_actual, nodo = heapq.heappop(cola_prioridad)

            for vecino, peso in self.grafo[nodo]:
                nueva_distancia = distancia_actual + peso
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    heapq.heappush(cola_prioridad, (nueva_distancia, vecino))

        return distancias

def construir_grafo():
    print("Ingrese el número total de vértices en el grafo:")
    num_vertices = int(input())
    grafo = Grafo(num_vertices)

    print("Ingrese las aristas en el formato 'origen destino peso' (ingrese 'fin' para terminar):")
    while True:
        entrada = input()
        if entrada.lower() == "fin":
            break
        origen, destino, peso = map(int, entrada.split())
        grafo.agregar_arista(destino, origen, peso)  # Invertir las aristas para calcular desde el destino hacia todos

    return grafo

if __name__ == "__main__":
    print("\n=== Caminos Mínimos desde Todos los Vértices a un Destino ===")
    grafo = construir_grafo()

    print("\nIngrese el vértice destino:")
    destino = int(input())

    distancias = grafo.dijkstra_invertido(destino)

    print("\nCaminos mínimos desde todos los vértices al vértice destino:")
    for i, distancia in enumerate(distancias):
        if distancia == float('inf'):
            print(f"Vértice {i} -> {destino}: No hay camino")
        else:
            print(f"Vértice {i} -> {destino}: Distancia mínima = {distancia}")
