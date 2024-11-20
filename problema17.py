import heapq
from collections import defaultdict

class Grafo:
    def __init__(self, num_nodos):
        self.num_nodos = num_nodos
        self.grafo = defaultdict(list)

    def agregar_arista(self, origen, destino, tiempo):
        self.grafo[origen].append((destino, tiempo))
        self.grafo[destino].append((origen, tiempo))

    def dijkstra(self, inicio, destino):
        distancias = [float('inf')] * self.num_nodos
        distancias[inicio] = 0
        predecesores = [-1] * self.num_nodos

        cola_prioridad = [(0, inicio)]

        while cola_prioridad:
            tiempo_actual, nodo_actual = heapq.heappop(cola_prioridad)

            if nodo_actual == destino:
                break

            for vecino, peso in self.grafo[nodo_actual]:
                nueva_distancia = tiempo_actual + peso
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    predecesores[vecino] = nodo_actual
                    heapq.heappush(cola_prioridad, (nueva_distancia, vecino))

        return distancias, predecesores

    def reconstruir_camino(self, predecesores, destino):
        camino = []
        nodo = destino
        while nodo != -1:
            camino.append(nodo)
            nodo = predecesores[nodo]
        return camino[::-1]

def construir_grafo():
    print("Ingrese el número total de nodos en el grafo:")
    num_nodos = int(input())
    grafo = Grafo(num_nodos)

    print("Ingrese las conexiones entre las ciudades en el formato 'origen destino tiempo' (ingrese 'fin' para terminar):")
    while True:
        entrada = input()
        if entrada.lower() == "fin":
            break
        origen, destino, tiempo = map(int, entrada.split())
        grafo.agregar_arista(origen, destino, tiempo)

    return grafo

if __name__ == "__main__":
    print("\n=== Red de Carreteras en el Área Metropolitana ===")
    grafo = construir_grafo()

    print("\nIngrese el nodo de origen (ciudad dormitorio) y el nodo destino (centro de la ciudad):")
    inicio, destino = map(int, input().split())

    distancias, predecesores = grafo.dijkstra(inicio, destino)

    if distancias[destino] == float('inf'):
        print("\nNo hay conexión entre el nodo de origen y el nodo destino.")
    else:
        tiempo_minimo = distancias[destino]
        camino = grafo.reconstruir_camino(predecesores, destino)
        print(f"\nEl tiempo mínimo desde el nodo {inicio} al nodo {destino} es: {tiempo_minimo} unidades de tiempo.")
        print(f"La sucesión de nodos por los que debe pasar es: {' -> '.join(map(str, camino))}")
