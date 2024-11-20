from collections import defaultdict

class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.grafo = defaultdict(list)

    def agregar_arco(self, origen, destino):
        self.grafo[origen].append(destino)
        self.grafo[destino].append(origen)

    def mostrar_grafo(self):
        print("\nGrafo representado con listas de adyacencia:")
        for nodo, vecinos in self.grafo.items():
            print(f"  {nodo} -> {', '.join(map(str, vecinos))}")

    def tiene_ciclo_util(self, nodo, visitados, padre):
        visitados[nodo] = True
        for vecino in self.grafo[nodo]:

            if not visitados[vecino]:
                if self.tiene_ciclo_util(vecino, visitados, nodo):
                    return True
            elif vecino != padre:
                return True

        return False

    def tiene_ciclo(self):
        visitados = [False] * self.num_vertices

        for nodo in range(self.num_vertices):
            if not visitados[nodo]:  
                if self.tiene_ciclo_util(nodo, visitados, -1):
                    return True

        return False


def construir_grafo():
    num_vertices = 6 
    grafo = Grafo(num_vertices)

    
    arcos = [
        (0, 1), (1, 2), (2, 3),
        (3, 4), (4, 5), (2, 4)
    ]

    for origen, destino in arcos:
        grafo.agregar_arco(origen, destino)

    return grafo


if __name__ == "__main__":
    print("=== Detectar Ciclos en un Grafo No Dirigido ===")
    

    grafo = construir_grafo()
    grafo.mostrar_grafo()

    if grafo.tiene_ciclo():
        print("\nEl grafo contiene ciclos.")
    else:
        print("\nEl grafo NO contiene ciclos.")
