from codigo_documentado_2 import * #Del proyecto "codigo_documentado_2" se importan todas las clases

arbol = Arbol() #Se crea un objeto arbol de acuerdo a la clase arbol
arbol.agregar_nodo("1.e4", "e5") 
arbol.agregar_nodo("1.d4", "d5")
#Se agregan los nodos en el arbol

defensa = arbol.buscar_defensa("1.e4") #Se crea un objeto donde se guarda la función de busqueda 
print("La defensa correspondiente a la jugada es:", defensa) #Se imprime la defensa 