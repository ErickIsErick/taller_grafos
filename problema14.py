class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.aristas = []

    def agregar_arista(self, origen, destino, peso):
        self.aristas.append((peso, origen, destino))

    def encontrar(self, padre, i):
        if padre[i] == i:
            return i
        return self.encontrar(padre, padre[i])

    def union(self, padre, rango, x, y):
        xraiz = self.encontrar(padre, x)
        yraiz = self.encontrar(padre, y)

        if rango[xraiz] < rango[yraiz]:
            padre[xraiz] = yraiz
        elif rango[xraiz] > rango[yraiz]:
            padre[yraiz] = xraiz
        else:
            padre[yraiz] = xraiz
            rango[xraiz] += 1

    def kruskal(self):
        self.aristas.sort()
        padre = []
        rango = []
        arbol_expansion = []

        for nodo in range(self.num_vertices):
            padre.append(nodo)
            rango.append(0)

        e = 0
        i = 0

        while e < self.num_vertices - 1:
            peso, origen, destino = self.aristas[i]
            i += 1
            x = self.encontrar(padre, origen)
            y = self.encontrar(padre, destino)

            if x != y:
                e += 1
                arbol_expansion.append((origen, destino, peso))
                self.union(padre, rango, x, y)

        return arbol_expansion

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
    print("\n=== Árbol de Expansión Mínima (Algoritmo de Kruskal) ===")
    grafo = construir_grafo()

    arbol_expansion = grafo.kruskal()

    print("\nAristas del Árbol de Expansión Mínima:")
    for origen, destino, peso in arbol_expansion:
        print(f"{origen} - {destino}: {peso}")
