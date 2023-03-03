import csv
from tree import ArbolBinarioBusqueda

def agregar_nodos_desde_csv(arbol, nombre_archivo):
    # funcion que agrega nodos desde un archivo CSV
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo_csv:
        # abre el archivo CSV en lectura
        lector_csv = csv.reader(archivo_csv)
        # crea un objeto lector_csv para leer las filas del archivo CSV
        for fila in lector_csv:
            # itera a traves de las filas del archivo CSV
            nombre_nodo = fila[0]
            # el primer valor de la fila es el user
            id_nodo = fila[1]
            # el segundo valor de la fila es la id de spotify
            if id_nodo.isdigit():
                # convierte cualquier numero a entero
                id_nodo = int(id_nodo)
            else:
                # Si el id no es un numero, calcula su valor un valor numerico agregando un valor ASCII a sus caracteres
                id_nodo = sum([ord(c) for c in id_nodo])
            arbol.insertar(id_nodo, nombre_nodo)

arbol = ArbolBinarioBusqueda()
# crea un objeto ArbolBinarioBusqueda vacío

agregar_nodos_desde_csv(arbol, 'Punto_1/User_track_data.csv')
# Agrega nodos al árbol binario de búsqueda desde el archivo CSV "User_track_data.csv"
agregar_nodos_desde_csv(arbol, 'Punto_1/User_track_data_2.csv')
# Agrega nodos al árbol binario de búsqueda desde el archivo CSV "User_track_data_2.csv"
agregar_nodos_desde_csv(arbol, 'Punto_1/User_track_data_3.csv')
# Agrega nodos al árbol binario de búsqueda desde el archivo CSV "User_track_data_3.csv"


print("\nÁrbol canónico\n")#Imprimimos por nivel.
arbol.imprimir_por_nivel()
print("\n———————————————————————————————————————————————————————————————————————————————————————————————————————————")

#Eliminamos uno de los nodos.
arbol.eliminar(12179172375)

print("\n Después de eliminar\n")
#Volvemos a imprimir para ver el nodo eliminado.
arbol.imprimir_por_nivel()

#Buscamos un nodo cualquiera. En las otras funciones se es más util ésta.
arbol.buscar_nodo(2413)

print("\n———————————————————————————————————————————————————————————————————————————————————————————————————————————")

print("\n Altura del Nodo 2413. De nuestro árbol.\n")
#Imrpimimos la altura de un Nodo en el árbol.
arbol.imprimir_altura(2413)

print("\n———————————————————————————————————————————————————————————————————————————————————————————————————————————")

print("\n Abuelo del Nodo 2359 de nuestro árbol.\n")
#Imrpimimos el abuelo y el tio, si tienen, los mostrará.
arbol.imprimir_abuelo_y_tio_por_id(2359)



#Buscar un nodo específico en el árbol
#nodo_buscado = arbol.raiz.derecho.izquierdo
#print('Nodo buscado:', nodo_buscado.id, nodo_buscado.nombre)