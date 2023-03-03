from tree import Tree

tree = Tree()
tree.add_node("Recursos humanos", 600000.01)
tree.add_node("Marketing", 200000.02)
tree.add_node("Investigación y desarrollo", 200000.03)
tree.add_node("Otros gastos", 200000.04)
tree.add_node("Nómina", 300000.05)
tree.add_node("Beneficios", 150000.06)
tree.add_node("Capacitación", 150000.07)

print("Arbol antes de eliminar.\n")

tree.print_tree()


tree.delete_node(600000.01)
print("\n------------------------------------------------")

print("Árbol actualizado.\n")
tree.print_tree()

