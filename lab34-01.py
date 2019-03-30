from treelib import Tree, Node
#tworzenie drzewa
tree = Tree()
tree.create_node("Harry", "h") # korzen
tree.create_node("Jane", "j", parent="h")
tree.create_node("Bill", "b", parent="h")
tree.create_node("Diane", "d", parent="j")
tree.create_node("Mary", "m", parent="d")
tree.create_node("Harry", "h2", parent="j")
tree.create_node("Harry2", "h3", parent="h2")
tree.create_node("Harry", "h4", parent="h3")
#wyswietlenie drzewa
tree.show()
#wyswietlenie info o niektorych wierzcholkach
"""
x = tree.get_node("m")
print(x.tag)
print(x.identifier)
y = tree.parent("m")
print(y.tag)
print(y.identifier)"""
z = tree.get_node("h2")

print ("rodic",z.bpointer)
print(z.tag)
print()
#print(z.is_root())





def dupilcate_node_path_check(tree,node):
#uzupelnij wnetrze funkcji
#byc moze warto skorzystac z petli
    
#petla dziala tak dlugo az zaglebi sie od node do korzenia
#petla robi przeskoki z wierzcholka na ojca
#gdy znajdziemy wierzcholki o tych samych tagach zwroc True
     
#w przeciwnym wypadku zwroc False
    current_node = node
    

    while  current_node.is_root() == False:
        current_node = tree.parent(current_node.identifier)
        print(current_node)
        if current_node.tag == node.tag :#(i id korzenia)
            print()
            return True, print("true",current_node)
    
        return False,print("false",current_node)


x = tree.get_node("h4")
print(dupilcate_node_path_check(tree,x))
#x = tree.get_node("m")
#print(dupilcate_node_path_check(tree,x))





