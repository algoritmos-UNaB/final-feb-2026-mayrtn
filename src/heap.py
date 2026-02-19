#Implementa un min‑heap 1‑indexado para ofertas (fin_fecha, titulo) con push, pop_min y build_heap(arr). 
#Genera 5 ofertas con fin_fecha = base + i*(S mod 4 + 1) y muestra el arreglo tras cada push y dos pop_min. 

import json

def cargar_s(archivo_nombre):
    with open(archivo_nombre, 'r') as f:
        data_estudiante = json.load(f)
        dni_ult = data_estudiante["dni_termina"]
        dia_ex = data_estudiante["dia_examen"]
        return ((dni_ult + dia_ex) % 17) + 3

s = cargar_s('student.json')
print(f"s derivada: {s}")

class heap_ofertas:
    def __init__(self):
        self.arreglo_heap = [None]

    def push(self, nueva_oferta):
        self.arreglo_heap.append(nueva_oferta)
        self.flotar_elemento(len(self.arreglo_heap) - 1)
        print(f"tras push {nueva_oferta[1]}: {self.arreglo_heap[1:]}")

    def flotar_elemento(self, i):
        while i > 1 and self.arreglo_heap[i][0] < self.arreglo_heap[i // 2][0]:
            temp = self.arreglo_heap[i]
            self.arreglo_heap[i] = self.arreglo_heap[i // 2]
            self.arreglo_heap[i // 2] = temp
            i = i // 2

    def pop_min(self):
        if len(self.arreglo_heap) <= 1:
            return None
      
        el_minimo = self.arreglo_heap[1]
        
        ultimo = self.arreglo_heap.pop()
        if len(self.arreglo_heap) > 1:
            self.arreglo_heap[1] = ultimo
            self.hundirElemento(1)
            
        print(f"tras pop_min: {self.arreglo_heap[1:]}")
        return el_minimo

    def hundirElemento(self, i): 
        n = len(self.arreglo_heap) - 1
        while 2 * i <= n:
            hijo_menor = 2 * i
            if hijo_menor + 1 <= n and self.arreglo_heap[hijo_menor + 1][0] < self.arreglo_heap[hijo_menor][0]:
                hijo_menor = hijo_menor + 1
           
            if self.arreglo_heap[i][0] <= self.arreglo_heap[hijo_menor][0]:
                break
 
            self.arreglo_heap[i], self.arreglo_heap[hijo_menor] = self.arreglo_heap[hijo_menor], self.arreglo_heap[i]
            i = hijo_menor

    def build_heap(self, lista_inicial):
        self.arreglo_heap = [None] + lista_inicial
        for j in range((len(self.arreglo_heap)-1)//2, 0, -1):
            self.hundirElemento(j)



mi_heap = heap_ofertas()
base_fecha = 20260000 
salto = (s % 4) + 1 

print("Generando las 5 ofertas...")
for i in range(1, 6):
    f_vencimiento = base_fecha + i * salto
    oferta_nueva = (f_vencimiento, f"oferta_{i}")
    mi_heap.push(oferta_nueva)

print("\nsacando los dos minimos:")
mi_heap.pop_min()
mi_heap.pop_min()
