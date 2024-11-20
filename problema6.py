from collections import defaultdict, deque


class Grafo:
    def __init__(self):
        self.grafo = defaultdict(list)  

    def agregar_arista(self, origen, destino):
        self.grafo[origen].append(destino)
        self.grafo[destino].append(origen)

    def mostrar_grafo(self):
        print("\nGrafo representado con listas de adyacencia:")
        for nodo, vecinos in self.grafo.items():
            print(f"  {nodo} -> {', '.join(map(str, vecinos))}")

    def es_conexo(self):
        
        visitados = set()
        cola = deque([next(iter(self.grafo))])  
        while cola:
            nodo = cola.popleft()
            if nodo not in visitados:
                visitados.add(nodo)
                for vecino in self.grafo[nodo]:
                    if vecino not in visitados:
                        cola.append(vecino)
        return len(visitados) == len(self.grafo)

    def tiene_camino_euler(self):
        if not self.es_conexo():
            return False, None

        impares = [nodo for nodo in self.grafo if len(self.grafo[nodo]) % 2 != 0]
        if len(impares) == 0:
            return True, "circuito"  
        elif len(impares) == 2:
            return True, "camino"  
        return False, None

    def encontrar_camino_euler(self):
        valido, tipo = self.tiene_camino_euler()
        if not valido:
            print("\nEl grafo no tiene un camino de Euler.")
            return

        print(f"\nEl grafo tiene un {tipo} de Euler.")
        
        pila = []
        camino = []
        arista_actual = next(iter(self.grafo)) 

        while pila or self.grafo[arista_actual]:
            if not self.grafo[arista_actual]:
                camino.append(arista_actual)
                arista_actual = pila.pop()
            else:
                pila.append(arista_actual)
                vecino = self.grafo[arista_actual].pop()
                self.grafo[vecino].remove(arista_actual)
                arista_actual = vecino

        camino.append(arista_actual)
        print("Camino de Euler:", " -> ".join(map(str, camino[::-1])))



def construir_grafo():
    grafo = Grafo()

    arcos = [
        (0, 1), (1, 2), (2, 3), (3, 0), (0, 2),
        (1, 3)
    ]

    for origen, destino in arcos:
        grafo.agregar_arista(origen, destino)

    return grafo


if __name__ == "__main__":
    print("=== Camino de Euler en un Grafo ===")

    
    grafo = construir_grafo()

    grafo.mostrar_grafo()

    # Encontrar y mostrar el camino de Euler
    grafo.encontrar_camino_euler()
