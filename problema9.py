from collections import defaultdict

class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.grafo = defaultdict(list)

    def agregar_arista(self, origen, destino):
        self.grafo[origen].append(destino)
        self.grafo[destino].append(origen)

    def dfs(self, u, visitados, parent, tiempo, low, disc, rutas_criticas):
        visitados[u] = True
        disc[u] = tiempo
        low[u] = tiempo
        tiempo += 1

        for v in self.grafo[u]:
            if not visitados[v]:
                parent[v] = u
                self.dfs(v, visitados, parent, tiempo, low, disc, rutas_criticas)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    rutas_criticas.append((u, v))
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    def encontrar_rutas_criticas(self):
        visitados = [False] * self.num_vertices
        disc = [float("Inf")] * self.num_vertices
        low = [float("Inf")] * self.num_vertices
        parent = [-1] * self.num_vertices
        rutas_criticas = []

        for i in range(self.num_vertices):
            if not visitados[i]:
                self.dfs(i, visitados, parent, 0, low, disc, rutas_criticas)

        return rutas_criticas


def construir_grafo():
    print("Ingrese el número total de vértices:")
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
    print("\n=== Encontrar Rutas Críticas en un Grafo ===")
    grafo = construir_grafo()
    rutas_criticas = grafo.encontrar_rutas_criticas()

    print("\nLas rutas críticas (aristas puente) del grafo son:")
    for u, v in rutas_criticas:
        print(f"{u} - {v}")
