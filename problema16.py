import heapq
from collections import defaultdict

class CentroDistribucion:
    def __init__(self, num_centros):
        self.num_centros = num_centros
        self.grafo = defaultdict(list)
        self.stock = defaultdict(dict)

    def agregar_arista(self, origen, destino, distancia):
        self.grafo[origen].append((destino, distancia))

    def agregar_stock(self, centro, articulo, cantidad):
        self.stock[centro][articulo] = cantidad

    def encontrar_centro_mas_cercano(self, centro_origen, articulo):
        distancias = [float('inf')] * self.num_centros
        distancias[centro_origen] = 0

        cola_prioridad = [(0, centro_origen)]
        while cola_prioridad:
            distancia_actual, centro_actual = heapq.heappop(cola_prioridad)

            if articulo in self.stock[centro_actual] and self.stock[centro_actual][articulo] > 0:
                return centro_actual, distancia_actual

            for vecino, peso in self.grafo[centro_actual]:
                nueva_distancia = distancia_actual + peso
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    heapq.heappush(cola_prioridad, (nueva_distancia, vecino))

        return None, None

def construir_red():
    print("Ingrese el número total de centros de distribución:")
    num_centros = int(input())
    red = CentroDistribucion(num_centros)

    print("Ingrese las conexiones entre los centros en el formato 'origen destino distancia' (ingrese 'fin' para terminar):")
    while True:
        entrada = input()
        if entrada.lower() == "fin":
            break
        origen, destino, distancia = map(int, entrada.split())
        red.agregar_arista(origen, destino, distancia)

    print("\nIngrese el stock de los centros en el formato 'centro articulo cantidad' (ingrese 'fin' para terminar):")
    while True:
        entrada = input()
        if entrada.lower() == "fin":
            break
        centro, articulo, cantidad = map(int, entrada.split())
        red.agregar_stock(centro, articulo, cantidad)

    return red

if __name__ == "__main__":
    print("\n=== Red de Centros de Distribución ===")
    red = construir_red()

    print("\nIngrese el centro origen y el artículo requerido en el formato 'centro_origen articulo':")
    centro_origen, articulo = map(int, input().split())

    centro_cercano, distancia = red.encontrar_centro_mas_cercano(centro_origen, articulo)

    if centro_cercano is not None:
        print(f"\nEl centro más cercano que tiene el artículo {articulo} es el centro {centro_cercano}, a una distancia de {distancia} km.")
    else:
        print(f"\nNo hay ningún centro que tenga el artículo {articulo} disponible.")
