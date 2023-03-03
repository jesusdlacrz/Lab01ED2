
# Creamos la clase del objeto tipo Node.
class Node:
    def __init__(self, category, amount):
        self.category = category #Almacena la categoría del nodo. (Categoría donde va dirigida el presupuesto)
        self.amount = amount #Almacena el monto del nodo. (Cantidad de dinero invertida en la categoría correspondiente)
        self.left = None # Puntero al hijo izquierdo del nodo en cuestión.
        self.right = None # Puntero hijo derecho del nodo en cuestión