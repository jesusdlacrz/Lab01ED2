import csv
from node import NodoArbol
from collections import deque

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, id, nombre):

        nuevo_nodo = NodoArbol(id, nombre)

        # si la raiz del arbol es nula, el nuevo nodo se establece como la raiz del arbol 
        if self.raiz is None:
            self.raiz = nuevo_nodo
            return True
        # si la raiz no es nula, creamos un bucle que continue hasta que se inserte un nuevo nodo en el arbol o se determine que ya existe un nodo con la misma id
        nodo_actual = self.raiz
        while nodo_actual is not None:

            # si ya existe un nodo con el mismo id, la funcion devuelve False y el nuevo nodo no se inserta
            if nuevo_nodo.id == nodo_actual.id:
                return False

            # Si el id del nuevo nodo es menor que el id del nodo actual, se verifica si el hijo izq del nodo actual es nulo
            # en ese caso, el nuevo nodo se inserta como el hijo izquierdo del nodo actual y la función retorna true
            elif nuevo_nodo.id < nodo_actual.id:
                if nodo_actual.izquierdo is None:
                    nodo_actual.izquierdo = nuevo_nodo
                    return True
                else:
                    nodo_actual = nodo_actual.izquierdo

            # Si el id del nuevo nodo es mayor que el id del nodo actual, se verifica si el hijo der del nodo actual es nulo
            # en ese caso, el nuevo nodo se inserta como el hijo derecho del nodo actual y la funcion retorna true
            else:
                if nodo_actual.derecho is None:
                    nodo_actual.derecho = nuevo_nodo
                    return True
                else:
                    nodo_actual = nodo_actual.derecho

        #si el ciclo termina sin haber insertado el nodo, se asume que se ha insertado correcctamente y se retorna true

        return True

    def imprimir_en_orden(self, nodo_actual):
        if nodo_actual is not None:
            self.imprimir_en_orden(nodo_actual.izquierdo)
            print(nodo_actual.id, nodo_actual.nombre)
            self.imprimir_en_orden(nodo_actual.derecho)
    
    def eliminar(self, id):
        # buscar el nodo a eliminar y su padre
        nodo_actual = self.raiz
        padre_actual = None
        while nodo_actual is not None and nodo_actual.id != id:
            padre_actual = nodo_actual
            if id < nodo_actual.id:
                nodo_actual = nodo_actual.izquierdo
            else:
                nodo_actual = nodo_actual.derecho

        # si el nodo no se encuentra, no se puede eliminar
        if nodo_actual is None:
            return False

            #verifica si el nodo actual no tiene hijos.
        if nodo_actual.izquierdo is None and nodo_actual.derecho is None:
            # si el nodo actual no tiene hijos, se elimina del arbol
            # si el nodo actual no es la raíz del arbol, se actualiza su padre para que ya no apunta al nodo actual
            if nodo_actual != self.raiz:
                if padre_actual.izquierdo == nodo_actual:
                    padre_actual.izquierdo = None
                else:
                    padre_actual.derecho = None
            # si el nodo actual es la raiz del árbol, se establece la raiz como None
            else:
                self.raiz = None

        # hijo a la derecha del nodo actual
        elif nodo_actual.izquierdo is None:
            hijo = nodo_actual.derecho
            nodo_actual.id = hijo.id
            nodo_actual.nombre = hijo.nombre
            nodo_actual.izquierdo = hijo.izquier
            

        # hijo a la izq del nodo actual
        elif nodo_actual.derecho is None:
            hijo = nodo_actual.izquierdo
            nodo_actual.id = hijo.id
            nodo_actual.nombre = hijo.nombre
            nodo_actual.izquierdo = hijo.izquierdo
            nodo_actual.derecho = hijo.derecho

        # tiene 2 hijos
        else:
            padre_sucesor = nodo_actual
            sucesor = nodo_actual.derecho
            while sucesor.izquierdo is not None:
                padre_sucesor = sucesor
                sucesor = sucesor.izquierdo

            # reemplazar el nodo eliminado por el sucesor
            nodo_actual.id = sucesor.id
            nodo_actual.nombre = sucesor.nombre

            # eliminar al sucesor
            if sucesor == padre_sucesor.izquierdo:
                padre_sucesor.izquierdo = sucesor.derecho
            else:
                padre_sucesor.derecho = sucesor.derecho
        return True
    
    def buscar_nodo(self, id):
        nodo_actual = self.raiz
        while nodo_actual is not None:
            if nodo_actual.id == id:
                return nodo_actual
            elif id < nodo_actual.id:
                nodo_actual = nodo_actual.izquierdo
            else:
                nodo_actual = nodo_actual.derecho
        return None  # el nodo no se encuentra en el arbol
    
    
    def imprimir_por_nivel(self):
        if self.raiz is None:
            return

        # se crea una cola y agregamos la raíz del árbol
        cola = deque()
        cola.append(self.raiz)

        # mientras la cola no este vacía, se procesan los nodos
        while cola:
            # se expulsa el primer elemento de la cola y es procesado
            nodo_actual = cola.popleft()
            print(nodo_actual.id, nodo_actual.nombre)

            # se agregan los hijos del nodo a la cola, si es que tienen alguno
            if nodo_actual.izquierdo is not None:
                cola.append(nodo_actual.izquierdo)
            if nodo_actual.derecho is not None:
                cola.append(nodo_actual.derecho)

    def altura(self, nodo_actual):
        # funcion que calcula la altura o nivel de un nodo en el arbol

        if nodo_actual is None:
            # si el nodo actual es vacio, al altura es 0 al no tener hijos
            return 0
        else:
            # si el nodo actual tiene hijos, calculamos la altura o nivel de cada uno y retornamos la altura max + 1, 
            # porque se cuenta el nodo actual como altura adicional
            altura_izq = self.altura(nodo_actual.izquierdo)
            altura_der = self.altura(nodo_actual.derecho)
            return max(altura_izq, altura_der) + 1

    def imprimir_altura(self, id):
        # funcion que imprime la altura de un nodo dado segun su id

        nodo = self.buscar_nodo(id)
        if nodo is None:
            # si el nodo no se encuentra en el arbol, se imprime:
            print("El nodo con ID " + str(id) + " no se encuentra en el árbol.")
        else:
            # si el nodo se encuentra en el arbol, se imprime:
            altura = self.altura(nodo)
            print("La altura del nodo con ID " + str(id) + " es " + str(altura))

    
    def encontrar_padre(self, nodo):
        padre_actual = None
        nodo_actual = self.raiz

    # recorre el arbol hasta que se encuentra el nodo o hasta que no haya más nodos que revisar
        while nodo_actual is not None:
            if nodo_actual.id == nodo.id: # si se encuentra el nodo, devuelve el padre actual
                return padre_actual
            elif nodo_actual.id > nodo.id: # si el id del nodo actual es mayor que el del nodo buscado, revisa el subárbol izquierdo
                padre_actual = nodo_actual
                nodo_actual = nodo_actual.izquierdo
            else: # si el id del nodo actual es menor que el del nodo buscado, revisa el subárbol derecho
                padre_actual = nodo_actual
                nodo_actual = nodo_actual.derecho

        # si no se encuentra el nodo, devuelve None
        return None


    def encontrar_abuelo(self, nodo):
        padre = self.encontrar_padre(nodo)
        if padre is not None: # si el nodo tiene padre, se busca su abuelo
            return self.encontrar_padre(padre)
        return None

    
    def encontrar_tio(self, nodo):
        padre = self.encontrar_padre(nodo)
        if padre is None: # si el nodo no tiene padre, no tiene tio
            return None

        if padre == self.raiz: # si el padre es la raiz, no tiene tio
            return None

        abuelo = self.encontrar_abuelo(nodo)
        if abuelo is None: # si el nodo no tiene abuelo, no tiene tio
            return None

        # si el padre del nodo es el hijo izquierdo del abuelo, el tio es el hijo derecho del abuelo (y al reves)
        if abuelo.izquierdo == padre:
            return abuelo.derecho
        else:
            return abuelo.izquierdo

        #nombre evidente
    def imprimir_abuelo_y_tio_por_id(self, id_nodo):
        nodo = self.buscar_nodo(id_nodo)
        if nodo is None: # si el nodo no se encuentra en el arbol, muestra este mensaje de error
            print("el nodo con el id {} no se encuentra en el arbol.".format(id_nodo))
            return

        # busca el abuelo y muestra su id (o un mensaje si el nodo no tiene abuelo)
        abuelo = self.encontrar_abuelo(nodo)
        if abuelo is not None:
            print("el abuelo del nodo con id {} es el nodo con id {}.".format(nodo.id, abuelo.id))
        else:
            print("el nodo con id {} no tiene abuelo.".format(nodo.id))

        # busca el tio y muestra su id (o un mensaje si el nodo no tiene tío)
        tio = self.encontrar_tio(nodo)
        if tio is not None:
            print("el tío del nodo con id {} es el nodo con id {}.".format(nodo.id, tio.id))
        else:
                print("el nodo con id {} no tiene tío.".format(nodo.id))

