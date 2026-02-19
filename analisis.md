1. Encapsulamiento e Interfaces (12 pts):
   
Una interfaz define que debe hacer una clase, es decir los metodos que debe tener como minimo.  En el contexto de un catalogo como Steam, si tenemos una clase 'catalogo' la interfaz garantiza que se van a implementar metodos como obetener_catalogo_completo() o mostrar_categorias().

Interfaces para las entidades mencionadas (S = 15)

**'Juego'**
invariante: el precio del juego nunca puede ser un valor negativo
postcondicion: al aplicar un descuento, el precio no puede ser menor que s
precondicion: al cargar un nuevo juego, el precio no puede ser null

**'Catalogo'**
invariante: el catalogo no puede contener 2 o mas juegos con el mismo id
precondicion: para buscar un juego por nombre, el usuario debe ingresar por lo menos 3 caracteres
postcondicion: al filtrar por mas vendidos el primer juego de la lista tiene que tener un numero de ventas superiores al segundo

**'usuario'**
invariante: el nombre de usuario tiene que tener al menos s caracteres
precondicion: para registrar un nuevo usuario debe ingresar un mail valido
postcondicion: al comprar un juego, el juego tiene que aparecer en la lista de juegos disponibles del usuario

**'Reseña'**
invariante: el puntaje debe ser un numero entre 1 y 5
precondicion: el usuario debe tener al menos 3 juegos en su biblioteca para poder escribir una reseña
postcondicion: al listar las reseñas, se deben mostrar primero las que tengan mas de s likes

El **encapsulamiento** nos proteje de la posibilidad de modifcar un objeto a traves de una variable, a traves del uso de atributos privadoos ( lo que nos obliga a modificar los objetos a traves de metodos especificos) y devolviendo copias de los objetos en vez del objeto en si. 

2. Estructuras de Datos Recursivas (10 pts)

Listas: Estructura lineal donde cada elemento tiene un único sucesor.Árbol: Estructura jerárquica no lineal donde cada nodo tiene un único padre.

Grafos: Conjunto de nodos conectados por aristas. Las conexiones no son jerárquicas sino relacionales.Representaciones de Grafos (V = 8, E = 19)

Matriz de Adyacencia: Matriz de $V \times V$ donde el valor en $(i, j)$ indica si existe una arista.

Lista de Adyacencia: Lista donde cada nodo tiene una sublista con sus vecinos directos.

Dado que para mis valores el grafo es denso (muchas aristas y pocos nodos), la Matriz de Adyacencia es eficiente para consultas rápidas. Sin embargo, para la implementación del TP se prefirió Lista de Adyacencia por su facilidad para implementar recorridos como BFS y DFS.

3. Análisis de Algoritmos (12 pts)

Ómicron: Cota superior. El peor escenario posible de ejecución.

Omega: Cota inferior. El mejor escenario posible.

Theta: Cota ajustada. El comportamiento promedio o exacto cuando omicron y omega coinciden.

Búsqueda por Prefijo en ABB
Peor Caso: omicron(n) si el árbol está desbalanceado (una lista).
Mejor/Promedio: omicron (log n) si el árbol está balanceado.

Se utiliza el orden lexicográfico de los títulos. Si el prefijo buscado es mayor al título del nodo actual, se descarta toda la rama izquierda (poda), esto reduce el espacio de búsqueda.


