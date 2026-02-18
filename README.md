[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/3yY8kq6c)
# Estructuras de Datos. FINAL – FEBRERO – 18 / 02 / 2026

### Tema Central: Sistema catálogo de videojuegos (estilo Steam)

### Instrucciones Generales
- Responde todas las preguntas utilizando exclusivamente Python para las partes prácticas.
- Personalización obligatoria anti‑IA: define `S = ((últimos 3 dígitos del DNI) + (día del examen)) mod 17 + 3` y úsalo en tamaños, desempates y ejemplos.
- Incluye en tu entrega una portada con `DNI`, `S` y ejemplos concretos que dependan de `S`.
- Sin librerías externas ni acceso a internet/modelos de IA.
- Duración: 4 horas. Total: 100 puntos. 8 ejercicios.

Material permitido: apuntes y libros de la bibliografía obligatoria del programa.

---

## Parte Teórica

1. Encapsulamiento e Interfaces (12 pts)
   - En el contexto de un catálogo tipo Steam, define qué es una interfaz en Programación Orientada a Objetos. Propón una interfaz para `Catalogo`, `Juego`, `Usuario` y `Reseña` con pre/post condiciones e invariantes (al menos 3 por clase, 2 deben depender de `S`, p. ej. longitud mínima de `id_interno` ≥ `S`). Explica cómo el encapsulamiento evita inconsistencias ante aliasing.

2. Estructuras de Datos Recursivas (10 pts)
   - En el catálogo, los géneros y subgéneros forman una jerarquía. Define listas, árboles y grafos; describe 2 representaciones para grafos (matriz y listas de adyacencia) y fundamenta cuándo elegir cada una considerando `V = 8 + (S mod 5)` y `E = 2V + (S mod 4)`.

3. Análisis de Algoritmos (12 pts)
   - Explica O(), Ω y Θ. Deriva las complejidades (mejor/promedio/peor caso) para buscar por prefijo en un ABB de títulos y justifica podas por orden lexicográfico. Plantea una recurrencia para `top_k` por partición y discute su solución asintótica (no es necesario resolverla formalmente).

4. Caminos Mínimos y NP (10 pts)
   - Distingue problemas en NP de NP‑completos. Explica por qué el camino mínimo con pesos no negativos se resuelve con Dijkstra y cuándo conviene DP sobre DAG (orden topológico). Indica por qué Dijkstra falla con pesos negativos y qué alternativa usar.

---

## Parte Práctica

5. Árbol Binario de Búsqueda (ABB) de Juegos (12 pts)
   - Implementa en Python `insert(titulo, juego)`, `buscar(titulo)`, `inorden()` y `buscar_prefix(prefijo)` (puede recorrer y podar por lexicográfico; no se exige análisis amortizado ni casos extremos). Construye el ABB con `m = 6 + (S mod 5)` títulos y muestra el `inorden`.

6. Heap Binaria – Ofertas (12 pts)
   - Implementa un min‑heap 1‑indexado para ofertas `(fin_fecha, titulo)` con `push`, `pop_min` y `build_heap(arr)`. Genera 5 ofertas con `fin_fecha = base + i*(S mod 4 + 1)` y muestra el arreglo tras cada `push` y dos `pop_min`. (Opcional +2 pts: `merge_k_streams`).

7. Grafos: BFS y DFS (12 pts)
   - Construye un grafo dirigido `G` con juegos como nodos (`V = 8 + (S mod 5)`) y aristas “jugar `a` sugiere `b`” (`E = 2V + (S mod 4)`). Representa por listas de adyacencia e implementa:
     - `bfs(origen)` que devuelva árbol BFS y distancias en número de aristas.
     - `dfs(origen)` que clasifique aristas (árbol, retroceso, avance, cruzadas) con tiempos de entrada/salida.
   - Ejecuta una BFS desde el nodo `idx == S mod V` y dibuja el árbol. (Opcional +2 pts: `scc_kosaraju` o `tarjan`).

8. DAG: Ordenamiento Topológico, Caminos Mínimos y MST (56 pts totales práctica → este ejercicio vale 20 pts)
   - Dependencias de DLC en DAG `D` con `V_D = 6 + (S mod 4)`:
     - Implementa `topo_kahn()` y muestra brevemente el orden obtenido (no se exige traza completa de la cola; sí justificar desempates por `hash(nombre) mod S`).
     - Resuelve el camino mínimo desde un origen con DP en orden topológico; justifica corrección.
   - Red no dirigida `R` con `V_R = 5 + (S mod 4)`, pesos enteros: implementa **uno** de los dos (`prim()` o `kruskal()`) y ejecuta manualmente mostrando la selección y manejo de empates.

---

### Requisitos de entrega
- Código Python en módulos separados (puede ser `src/`): `poo.py`, `listas.py`, `abb.py`, `arbol_generico.py`, `heap.py`, `grafos.py`, `dag.py`, `mst.py`.
- Documento `analisis.md` (o `analisis.pdf`) con: trazas manuales, invariantes y justificaciones, recorridos dibujados y análisis de complejidad (O/Ω/Θ; discusión de recurrencias cuando corresponda).
- Incluir `student.json` con `dni` y `exam_day`; el código debe leerlo para derivar `S`."