from collections import defaultdict

class Grafo:
    def __init__(self, num_comunidades):
        self.num_comunidades = num_comunidades
        self.grafo = defaultdict(list)

    def agregar_arista(self, origen, destino, peso):
        self.grafo[origen].append((destino, peso))

    def mostrar_grafo(self):
        print("\nGrafo representado con listas de adyacencia:")
        for nodo, vecinos in self.grafo.items():
            print(f"  {nodo} -> {', '.join([f'{v} (personas: {p})' for v, p in vecinos])}")

    def analizar_fuentes_sumideros(self):
        entrada = [0] * self.num_comunidades
        salida = [0] * self.num_comunidades

        for origen, vecinos in self.grafo.items():
            salida[origen] += len(vecinos)
            for destino, _ in vecinos:
                entrada[destino] += 1

        fuentes = [i for i in range(self.num_comunidades) if entrada[i] == 0 and salida[i] > 0]
        sumideros = [i for i in range(self.num_comunidades) if salida[i] == 0 and entrada[i] > 0]

        print("\nAnálisis de fuentes y sumideros:")
        print(f"Fuentes (solo tienen aristas de salida): {fuentes if fuentes else 'Ninguna'}")
        print(f"Sumideros (solo tienen aristas de entrada): {sumideros if sumideros else 'Ninguno'}")


def construir_grafo():
    num_comunidades = 12
    grafo = Grafo(num_comunidades)


    desplazamientos = [
        (0, 1, 10), (0, 2, 5), (1, 3, 15), (2, 4, 20),
        (3, 5, 25), (4, 6, 30), (5, 7, 10), (6, 8, 15),
        (7, 9, 5), (8, 10, 10), (9, 11, 20), (10, 11, 5)
    ]

    for origen, destino, peso in desplazamientos:
        grafo.agregar_arista(origen, destino, peso)

    return grafo

# Programa principal
if __name__ == "__main__":
    print("=== Grafo de Desplazamientos entre Comunidades ===")

    grafo = construir_grafo()

    grafo.mostrar_grafo()

    grafo.analizar_fuentes_sumideros()
