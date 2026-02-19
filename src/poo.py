class Juego:
    def __init__(self, titulo, precio, id_interno):
        if precio < 0:
            self._precio = 0
        else:
            self._precio = precio
        
        self._titulo = titulo
        self._id_interno = id_interno 

    def aplicar_descuento(self, porcentaje, s_val):
        nuevo_precio = self._precio * (1 - porcentaje / 100)
        if nuevo_precio < s_val:
            self._precio = s_val
        else:
            self._precio = nuevo_precio
            
    def __str__(self):
        return f"Juego: {self._titulo} | Precio: ${self._precio:.2f}"

class Usuario:
    def __init__(self, nombre_user, email, s_val):
        if len(nombre_user) < s_val:
            self._nombre = "Usuario_por_defecto_largo"
        else:
            self._nombre = nombre_user
            
        self._email = email
        self.lista_juegos_comprados = [] 

    def comprar_juego(self, juego_obj):
        self.lista_juegos_comprados.append(juego_obj)
        print(f"Usuario {self._nombre} compro {juego_obj._titulo}")

class Reseña:
    def __init__(self, autor, puntaje, texto, likes):
        if 1 <= puntaje <= 5:
            self._puntos = puntaje
        else:
            self._puntos = 3 
            
        self._texto = texto
        self._likes = likes
        self._autor = autor

class Catalogo:
    def __init__(self):
        self._juegos_lista = {} 

    def agregar_juego(self, juego_obj):
        if juego_obj._id_interno not in self._juegos_lista:
            self._juegos_lista[juego_obj._id_interno] = juego_obj
        else:
            print("id repetido, no se carga")
