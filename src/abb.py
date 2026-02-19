#Árbol Binario de Búsqueda (ABB) de Juegos (12 pts)
#Implementa en Python insert(titulo, juego), buscar(titulo), inorden() y buscar_prefix(prefijo)
#(puede recorrer y podar por lexicográfico; no se exige análisis amortizado ni casos extremos). 
#Construye el ABB con m = 6 + (S mod 5) títulos y muestra el inorden.

import json

with open(archivo, 'r') as archivoJson:
        datos = json.load(archivoJson)
        dni = datos["dni_termina"] 
        dia_examen = datos["dia_examen"]
        return ((dni + dia_examen) % 17) + 3
    
s = cargar_s_desde_json('student.json')
print(f"Valor de s derivado: {s}")
  
class JuegoObjeto:
  def __init__ (self, titulo, precio, valoracion):
    self.titulo=titulo
    self.precio=precio
    self.valoracion=valoracion
  
class nodo:
  def __init__ (self, titulo, jeugo):
    self.titulo=titulo
    self.juego=juego
    self.izq=none
    self.der=none

class arbolJuegos:
  def __init__(self):
    self.raiz=none

  def insertar(self, titulo, juego):
    if self.raiz is None:
      self.raiz = nodo(titulo,jeugo)
    else:
      self._insertar_recursivamente(self.raiz, titulo, juego)

  def insertar_recursivamente(self, nodo, titulo, juego):
    if titulo < nodo.titulo 
      if nodo.izq is None:
        nodo.izq = nodo(titulo, juego)
    else: self.insertar_recursivamente(nodo.izq, titulo, juego)
    if titulo > nodo.titulo
      if nodo.der is None :
        nodo.der = nodo(titulo, juego)
    else: self.insertar_recursivamente(nodo.der, titulo, jeugo)

  def inorden(self):
    self.inorden_recurisivo(self.raiz)

def inorden_recursivo(self, nodo):
  if nodo is not None:
    self.inornde_recursivo(nodo.izq)
    print(nodo.titulo)
    self.inorden_recursivo(nodo.der)

def buscar(self, titulo):
  return self.buscar_recursivamente(self.raiz, titulo)

def buscar_recursivamente(self, nodo, titulo):
  if nodo is None:
    return None

if nodo.titulo == titulo:
return nodo.juego

if titulo>nodo.titulo:
  return self.buscar_recursivamente(nodo.izq, titulo)
else: 
  return self.buscar_recusrivamente(nodo.der, titulo)

def buscar_prefix(self, prefijo):
  lista=[]
  self.buscar_prefix_recursivamente(self.raiz, prefijo, lista)
  return lista

def buscar_prefix_recursivamente(self, prefijo)
  if nodo is None:
    return
  if nodo.titulo.startwith(prefijo)
    lista.append(nodo.titulo)
  if prefijo < nodo.titulo.startwith(prefijo)
    self.buscar_prefix_recursivamente(nodo.izq, prefijo, lista)
if prefijo >= nodo.titulo.startwith(prefijo)
    self.buscar_recursivamente(nodo.der, prefijo, lista)


catalogo = arbolJuegos()
lista_juegos = [
  JuegoObjeto("Age of Empires v", 500, 5),
  JuegoObjeto("GTA Vice City", 470, 4.6 ),
  JuegoObjeto("NFS Underground 2", 387, 4.8),
  JuegoObjeto("GTA San Andreas", 1300, 4.1),
  JuegoObjeto("Counter Strike", 150, 4.9 ),
  JuegoObjeto("Populus", 76, 3.4),
  JuegoObjeto("Minecraft", 1450, 4.4)
]

m = 6 + (s % 5)

for i in range(m):
    juego = lista_juegos[i % len(lista_juegos)]
    catalogo.insertar(juego.titulo, juego)

catalogo.inorden()

prefijo = "GTA"
print(f"Resultados para la busqueda ' {prefijo} ' : {catalogo.buscar_prefix(prefijo)}")
      
  


