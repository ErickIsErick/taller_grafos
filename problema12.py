import heapq
from collections import defaultdict

class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.grafo = defaultdict(list)

    def agregar_arista(self, origen, destino, peso):
        self.grafo[origen].append((destino, peso))
        self.grafo[destino].append((origen, peso))  # Grafo no dirigido

    def dijkstra(self, origen):
        distancias = [float('inf')] * self.num_vertices
        num_arcos = [float('inf')] * self.num_vertices
        distancias[origen] = 0
        num_arcos[origen] = 0

        cola_prioridad = [(0, 0, origen)]  # (distancia, arcos, nodo)
        visitados = set()

        while cola_prioridad:
            distancia_actual, arcos_actuales, nodo = heapq.heappop(cola_prioridad)

            if nodo in visitados:
                continue
            visitados.add(nodo)

            for vecino, peso in self.grafo[nodo]:
                nueva_distancia = distancia_actual + peso
                nuevos_arcos = arcos_actuales + 1

                if nueva_distancia < distancias[vecino] or (
                    nueva_distancia == distancias[vecino] and nuevos_arcos < num_arcos[vecino]
                ):
                    distancias[vecino] = nueva_distancia
                    num_arcos[vecino] = nuevos_arcos
                    heapq.heappush(cola_prioridad, (nueva_distancia, nuevos_arcos, vecino))

        return distancias, num_arcos

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
        grafo.agregar_arista(origen, destino, peso)

    return grafo

if __name__ == "__main__":
    print("\n=== Algoritmo de Dijkstra Modificado ===")
    grafo = construir_grafo()

    print("\nIngrese el vértice de origen:")
    origen = int(input())

    distancias, num_arcos = grafo.dijkstra(origen)

    print("\nResultados del algoritmo de Dijkstra modificado:")
    for i in range(len(distancias)):
        print(f"Vértice {i}: Distancia mínima = {distancias[i]}, Número de arcos = {num_arcos[i]}")
