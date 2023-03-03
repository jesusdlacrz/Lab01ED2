from node import Node

#Clase del objeto tipo árbol. (Donde se construyó el ÁRBOL)

class Tree:

    def __init__(self):
        self.root = None #Raíz del árbol.
    
    # Función pública para agregar nodos al árbol.
    def add_node(self, category, amount):
        if self.root is None: #En caso de que el árbol esté vacío, el nuevo nodo será la raíz.
            self.root = Node(category, amount)
        else:
            self._add_node_(category, amount, self.root) #En caso que no se cumpla lo de arriba, se debe llamar al método auxiliar, para agregar el nodo.
    
    # Función auxiliar para agregar un Nodo al árbol. Función privada.
    def _add_node_(self, category, amount, current_node):
        if amount < current_node.amount: #Si el monto es menor que el Nodo actual, se agrega al subárbol izquierdo.
            if current_node.left is None:
                current_node.left = Node(category, amount)
            else:
                #En caso de no cunmplirse lo último, pasamos el método al subárbol izquierdo, recursivamente.
                self._add_node_(category, amount, current_node.left) 
        else:
            if current_node.right is None: #Si el monto es menor que el Nodo actual, se agrega al subárbol izquierdo.
                current_node.right = Node(category, amount)
            else:
                #En caso de no cunmplirse lo último, pasamos el método al subárbol derecho, recursivamente.
                self._add_node_(category, amount, current_node.right)
    
    #Función para imprimir el árbol.
    def print_tree(self):
        if self.root is not None: #Validamos que el árbol no esté vacío.
            #En caso de cumplirse, le llamamos la función auxiliar. 
            self._print_tree_helper(self.root) 
    

    #Función auxiliar para imprimir el árbol de forma ascendente.

    def _print_tree_helper(self, current_node):
        if current_node is not None:
            self._print_tree_helper(current_node.left) #Se imprime el subárbol izquierdo
            print(f"{current_node.category}: {current_node.amount}") #Imprimimos el nodo actual.
            self._print_tree_helper(current_node.right) #Y por último el subárbol derecho.

    #Función para eliminar un Nodo del árbol.
    def delete_node(self, amount):
        self.root = self._delete_node_helper(amount, self.root)
    
    #Función auxiliar para eliminar un Nodo del árbol.
    def _delete_node_helper(self, amount, current_node):
        if current_node is None: #Se valida si nodo realmente está en el arbol.
            return current_node
            
        #Si el monto es menor que el Nodo actual, buscamos en el subárbol izquierdo.
        elif amount < current_node.amount: 
            #Llamamos recursivamente la función auxiliar, para el subárbol izquierdo.
            current_node.left = self._delete_node_helper(amount, current_node.left)
        
        #Si el monto es mayor que el Nodo actual, buscamos en el subárbol derecho.
        elif amount > current_node.amount:
            #Llamamos recursivamente la función auxiliar, para el subárbol derecho.
            current_node.right = self._delete_node_helper(amount, current_node.right)
        
        else: # Si encontramos el nodo que queremos eliminar.


            # Si el nodo no tiene hijos izquierdos, lo reemplazamos por su hijo derecho si tiene.
            if current_node.left is None:
                temp = current_node.right
                current_node = None
                return temp
            
            # Si el nodo no tiene hijos derechos, lo reemplazamos por su hijo izquierdo si tiene.
            elif current_node.right is None: 
                temp = current_node.left
                current_node = None
                return temp
            
                """
                En caso de que el nodo tenga dos hijos, tenemos que encontrar el sucesor de manera inorden, es decir, 
                el que esté más a la izquierda del subárbol derecho) y lo remplazamos por el nodo que queremos eliminar
                """
            else: 
                
                temp = self._find_min_node(current_node.right) #Buscamos el Nodo con monto mínimo en el súbarbol derecho.
                current_node.category = temp.category
                current_node.amount = temp.amount
                
                #Finalmente eliminamos el sucesor encontrado, recursivamente.
                current_node.right = self._delete_node_helper(temp.amount, current_node.right)

        return current_node #Retornamos el nodo actual.
    

    #Función para encontrar el Nodo con menor monto.
    def _find_min_node(self, current_node):

        #Mientras el Nodo actual tiene un hijo izquierdo.
        while current_node.left is not None:
            #Asignar el hijo izquierdo al nodo actual.
            current_node = current_node.left
        #Finalmente se retorna el Nodo actual.
        return current_node