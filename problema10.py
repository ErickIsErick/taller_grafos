from collections import defaultdict, deque

class PERT:
    def __init__(self, num_tareas):
        self.num_tareas = num_tareas
        self.grafo = defaultdict(list)
        self.pesos = {}

    def agregar_arco(self, origen, destino, peso):
        self.grafo[origen].append(destino)
        self.pesos[(origen, destino)] = peso

    def calcular_tiempos(self):
        grados_entrada = [0] * self.num_tareas
        for origen in self.grafo:
            for destino in self.grafo[origen]:
                grados_entrada[destino] += 1

        cola = deque()
        for i in range(self.num_tareas):
            if grados_entrada[i] == 0:
                cola.append(i)

        tiempos_inicio = [0] * self.num_tareas
        orden = []

        while cola:
            nodo = cola.popleft()
            orden.append(nodo)

            for vecino in self.grafo[nodo]:
                tiempos_inicio[vecino] = max(
                    tiempos_inicio[vecino], tiempos_inicio[nodo] + self.pesos[(nodo, vecino)]
                )
                grados_entrada[vecino] -= 1
                if grados_entrada[vecino] == 0:
                    cola.append(vecino)

        tiempo_total = max(tiempos_inicio)
        return tiempos_inicio, tiempo_total

def construir_pert():
    print("Ingrese el número total de tareas en la red PERT:")
    num_tareas = int(input())
    pert = PERT(num_tareas)

    print("Ingrese las dependencias en el formato 'origen destino peso' (ingrese 'fin' para terminar):")
    while True:
        entrada = input()
        if entrada.lower() == "fin":
            break
        origen, destino, peso = map(int, entrada.split())
        pert.agregar_arco(origen, destino, peso)

    return pert

if __name__ == "__main__":
    print("\n=== Análisis de Red PERT ===")
    pert = construir_pert()

    tiempos_inicio, tiempo_total = pert.calcular_tiempos()

    print("\nTiempos de inicio de cada tarea:")
    for i, tiempo in enumerate(tiempos_inicio):
        print(f"Tarea {i}: comienza en el tiempo {tiempo}")

    print(f"\nEl tiempo total para completar todas las tareas es: {tiempo_total}")
