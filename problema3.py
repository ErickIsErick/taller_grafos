from collections import defaultdict


class Nodo:
    def __init__(self):
        self.salen = []  
        self.entran = []  

# Clase para representar el grafo
class Grafo:
    def __init__(self, num_nodos):
        self.num_nodos = num_nodos
        self.nodos = defaultdict(Nodo)

    def agregar_arco(self, origen, destino, peso):
        self.nodos[origen].salen.append((destino, peso))
        self.nodos[destino].entran.append((origen, peso))

    def mostrar_grafo(self):
        print("\nRepresentación del grafo:")
        for nodo, data in self.nodos.items():
            print(f"Nodo {nodo}:")
            print(f"  Arcos que salen: {', '.join([f'{v} (peso: {p})' for v, p in data.salen])}")
            print(f"  Arcos que entran: {', '.join([f'{v} (peso: {p})' for v, p in data.entran])}")


def construir_grafo():
    num_comunidades = 12
    grafo = Grafo(num_comunidades)

    desplazamientos = [
        (0, 1, 10), (0, 2, 5), (1, 3, 15), (2, 4, 20),
        (3, 5, 25), (4, 6, 30), (5, 7, 10), (6, 8, 15),
        (7, 9, 5), (8, 10, 10), (9, 11, 20), (10, 11, 5)
    ]

    for origen, destino, peso in desplazamientos:
        grafo.agregar_arco(origen, destino, peso)

    return grafo


if __name__ == "__main__":
    print("=== Representación del Grafo con Listas Enlazadas ===")
    
    grafo = construir_grafo()

    grafo.mostrar_grafo()
