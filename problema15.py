from collections import defaultdict, deque

class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.grafo = defaultdict(list)
        self.grafo_reverso = defaultdict(list)

    def agregar_arista(self, origen, destino):
        self.grafo[origen].append(destino)
        self.grafo_reverso[destino].append(origen)

    def es_fuertemente_conexo(self):
        def dfs(nodo, visitados, grafo):
            visitados.add(nodo)
            for vecino in grafo[nodo]:
                if vecino not in visitados:
                    dfs(vecino, visitados, grafo)

        visitados = set()
        dfs(0, visitados, self.grafo)
        if len(visitados) != self.num_vertices:
            return False

        visitados.clear()
        dfs(0, visitados, self.grafo_reverso)
        return len(visitados) == self.num_vertices

    def verificar_grados(self):
        grados_entrada = [0] * self.num_vertices
        grados_salida = [0] * self.num_vertices

        for origen in self.grafo:
            grados_salida[origen] += len(self.grafo[origen])
            for destino in self.grafo[origen]:
                grados_entrada[destino] += 1

        for i in range(self.num_vertices):
            if grados_entrada[i] != grados_salida[i]:
                return False

        return True

    def encontrar_circuito_euler(self):
        if not self.es_fuertemente_conexo():
            print("\nEl grafo no es fuertemente conexo. No tiene un circuito de Euler.")
            return []

        if not self.verificar_grados():
            print("\nEl grafo no cumple la condición de grados de entrada y salida iguales. No tiene un circuito de Euler.")
            return []

        circuito = []
        pila = [0]

        while pila:
            nodo = pila[-1]
            if self.grafo[nodo]:
                vecino = self.grafo[nodo].pop()
                pila.append(vecino)
            else:
                circuito.append(pila.pop())

        return circuito[::-1]

def construir_grafo():
    print("Ingrese el número total de vértices en el grafo:")
    num_vertices = int(input())
    grafo = Grafo(num_vertices)

    print("Ingrese las aristas en el formato 'origen destino' (ingrese 'fin' para terminar):")
    while True:
        entrada = input()
        if entrada.lower() == "fin":
            break
        origen, destino = map(int, entrada.split())
        grafo.agregar_arista(origen, destino)

    return grafo

if __name__ == "__main__":
    print("\n=== Determinar y Encontrar Circuito de Euler en un Grafo Dirigido ===")
    grafo = construir_grafo()

    circuito = grafo.encontrar_circuito_euler()

    if circuito:
        print("\nEl grafo tiene un circuito de Euler:")
        print(" -> ".join(map(str, circuito)))
    else:
        print("\nNo se encontró un circuito de Euler en el grafo.")
