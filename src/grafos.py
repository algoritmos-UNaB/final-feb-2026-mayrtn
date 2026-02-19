#Construye un grafo dirigido G con juegos como nodos (V = 8 + (S mod 5)) y aristas “jugar a sugiere b” (E = 2V + (S mod 4)). 
#Representa por listas de adyacencia e implementa:
#bfs(origen) que devuelva árbol BFS y distancias en número de aristas.
#dfs(origen) que clasifique aristas (árbol, retroceso, avance, cruzadas) con tiempos de entrada/salida.
#Ejecuta una BFS desde el nodo idx == S mod V y dibuja el árbol. (Opcional +2 pts: scc_kosaraju o tarjan).

import json

with open(archivo, 'r') as archivoJson:
        datos = json.load(archivoJson)
        dni = datos["dni_termina"] 
        dia_examen = datos["dia_examen"]
        return ((dni + dia_examen) % 17) + 3
    
s = cargar_s_desde_json('student.json')
print(f"Valor de s derivado: {s}")

cant_nodos = 8 + (s % 5) 
cant_aristas = (2 * cant_nodos) + (s % 4)
inicio_bfs = s % cant_nodos

lista_adyacencia = {}
for i in range(cant_nodos):
    lista_adyacencia[i] = []

conexiones_juegos = [
    (0,1), (0,2), (1,2), (1,3), (2,4), (3,0), (3,5), (4,5), (4,6), (5,6),
    (5,7), (6,7), (6,0), (7,0), (7,1), (0,4), (1,5), (2,6), (3,7)
]

for origen, destino in conexiones_juegos:
    if origen in lista_adyacencia:
        lista_adyacencia[origen].append(destino)

def bfs(grafo, nodo_inicial):
    visitados = {nodo_inicial}
    cola_proceso = [(nodo_inicial, 0)]
    arbolBfs = []
    distancias_nodos = {nodo_inicial: 0}
    
    idx = 0
    while idx < len(cola_proceso):
        nodo_act, d = cola_proceso[idx]
        idx += 1
        
        for vesino in grafo[nodo_act]:
            if vesino not in visitados:
                visitados.add(vesino)
                distancias_nodos[vesino] = d + 1
                arbolBfs.append((nodo_act, vesino))
                cola_proceso.append((vesino, d + 1))
                
    return arbolBfs, distancias_nodos

t_entrada = {}
t_salida = {}
colores_nodos = {} 
reloj_global = 0

def dfs_principal(lista_adyasencias): 
    global reloj_global
    reloj_global = 0
    for n in lista_adyasencias:
        colores_nodos[n] = "blanco"
    
    for nodo in lista_adyasencias:
        if colores_nodos[nodo] == "blanco":
            visitar_dfs_recursivo(lista_adyasencias, nodo)

def visitar_dfs_recursivo(grafo_ady, u):
    global reloj_global
    reloj_global += 1
    t_entrada[u] = reloj_global
    colores_nodos[u] = "gris"
    
    for v in grafo_ady[u]:
        if colores_nodos[v] == "blanco":
            print(f"arista {u}-{v}: arbol")
            visitar_dfs_recursivo(grafo_ady, v)
        elif colores_nodos[v] == "gris":
            print(f"arista {u}-{v}: retroceso")
        elif colores_nodos[v] == "negro":
            if t_entrada[u] < t_entrada[v]:
                print(f"arista {u}-{v}: avance")
            else:
                print(f"arista {u}-{v}: crusada") 
                
    colores_nodos[u] = "negro"
    reloj_global += 1
    t_salida[u] = reloj_global


arbol_res, dists_res = bfs(lista_adyacencia, inicio_bfs)
print("Arbol BFS generado:", arbol_res)
print("Distancias encontradas:", dists_res)

dfs_principal(lista_adyacencia)
print("tiempos finales:")
for nodo_id in lista_adyacencia:
    print(f"juego {nodo_id}: {t_entrada[nodo_id]}/{t_salida[nodo_id]}")
