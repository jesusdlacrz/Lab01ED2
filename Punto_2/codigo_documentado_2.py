class Nodo: #Se define la clase nodo que representa a un nodo del arbol
    def __init__(self, jugada, defensa):
        #En el constructor se tiene la propiedad jugada en la cual se almacena la jugada que se realiza en el juego
        #y defensa que almacena la defensa correspondiente para cada jugada.
        self.jugada = jugada
        self.defensa = defensa
        #Se tienen como propiedades a self.izquierdo y self.derecho para mostras los punteros de los nodos   
        self.izquierdo = None
        self.derecho = None
        #self.evaluacion es aquella en al cual se almacenará la evaluación del nodo
        self.evaluacion = 0

class Arbol: #Se define la clase arbol
    def __init__(self):
        #Se define que la raiz es None para demostrar que inicialmente el arbol es vacío
        self.raiz = None
    
    def agregar_nodo(self, jugada, defensa): #Se define el metodo agregar_nodo
        #Este metodo funciona para agregar un nuevo nodo al arbol
        nuevo_nodo = Nodo(jugada, defensa) 
        if self.raiz is None: #En caso tal de que la raiz esté en None o vacía, el nuevo nodo agregado se convierte en la raíz
            self.raiz = nuevo_nodo
        else: #En el caso de que ya exista un nodo en la raíz se llama al metodo _agregar_nodo para agregar el nuevo nodo de manera recursiva
            self._agregar_nodo(self.raiz, nuevo_nodo)
    
    def _agregar_nodo(self, nodo_actual, nuevo_nodo): #Se define el metodo _agregar_nodo
        #Este metodo funciona para agregar un nuevo nodo al arbol pero utilizando recursividad
        #En caso tal de que la jugada actual sea igual a la jugada del nuevo nodo la defensa que tenia almacenada el nodo actual se actualiza con la defensa que tiene el nuevo nodo
        if nodo_actual.jugada == nuevo_nodo.jugada:
            nodo_actual.defensa = nuevo_nodo.defensa
        #En caso tal de que la jugada actual sea menor a la jugada del nuevo nodo se busca lugar para el nuevo nodo en el hijo izquierdo del nodo que se encuentra
        elif nuevo_nodo.jugada < nodo_actual.jugada:
            if nodo_actual.izquierdo is None: #Si el nodo hijo izquierdo actual es vacío, entonces se agrega a ese hijo izquierdo el nuevo nodo
                nodo_actual.izquierdo = nuevo_nodo
            else: #Si el hijo izquierdo no es vacío, entonces se llama al metodo de _agregar_nodo de manera recursiva en el hijo izquierdo, para así agregar el nuevo nodo
                self._agregar_nodo(nodo_actual.izquierdo, nuevo_nodo)
        #En caso tal de que la jugada actual sea mayor a la jugada del nuevo nodo se busca lugar para el nuevo nodo en el hijo derecho del nodo que se encuentra
        else:
            if nodo_actual.derecho is None: #De igual forma que con el hijo izquierdo si el nodo hijo derecho actual es vacío, entonces se agrega a ese hijo derecho el nuevo nodo
                nodo_actual.derecho = nuevo_nodo
            else: #Si no es vacío el hijo derecho, entonces se llama al metodo de _agregar_nodo_ de manera recursiva en el hijo derecho, para así agregar el nuevo nodo
                self._agregar_nodo(nodo_actual.derecho, nuevo_nodo)
    
    def buscar_defensa(self, jugada): #Se define el metodo buscar_defensa
        #Este metodo funciona para hacer busqueda de aquella defensa correspondiente a una respectiva jugada, tomando como parametros "jugada" que sería el movimiento en el juego que se quiere buscar 
        return self._buscar_defensa(self.raiz, jugada) #Se llama al metodo de _buscar_defensa para realizar la busqueda desde la raiz hasta la jugada que se busca (de manera recursiva)
    
    def _buscar_defensa(self, nodo_actual, jugada): #Se define el metodo _buscar_defensa
        #Este metodo funciona para buscar de manera recursiva la defensa acorde a una jugada en especifico en el arbol
        #Si el nodo actual es igual a None significa que la jugada que se busca no se encuentra en el arbol, con lo cual no devuelve nada
        if nodo_actual is None:
            return None
        #Si el nodo actual es igual a la jugada que se está buscando, quiere decir que se encontró la defensa que corresponde a esa jugada y devuelve la defensa almacenada en ese nodo actual
        elif nodo_actual.jugada == jugada:
            return nodo_actual.defensa
        #Si la jugada que se está buscando es menor a la jugada almacenada en el nodo actual, se comienza a busca en el subarbol izquierdo utilizando el metodo de _buscar_defensa de mandera recursiva
        elif jugada < nodo_actual.jugada:
            return self._buscar_defensa(nodo_actual.izquierdo, jugada)
        #Si la jugada que se está buscando resulta ser mayor a la jugada almacenada en el nodo actual, entonces se comienza a buscar en el subarbol derecho utilizando de la misma forma el metodo de _buscar_defensa de manera recursiva, pero esta vez con el hijo derecho
        else:
            return self._buscar_defensa(nodo_actual.derecho, jugada)