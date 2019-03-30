from treelib import Tree, Node
import time
 
def reachable_states(state):
    if state == "Gdansk":
        return [["Gdynia",24],["Koscierzyna",58],["Tczew",33],["Elblag",63]]
    if state == "Gdynia":
        return [["Gdansk",24],["Lebork",60],["Wladyslawowo",33]]
    if state == "Koscierzyna":
        return [["Gdansk",24],["Tczew",59],["Lebork",58],["Bytow",40],["Chojnice",70]]
    if state == "Chojnice":
        return [["Koscierzyna",70],["Bytow",65]]
    if state == "Bytow":
        return [["Chojnice",65],["Koscierzyna",40],["Slupsk",70]]
    if state == "Tczew":
        return [["Koscierzyna",59],["Gdansk",33],["Elblag",53]]
    if state == "Elblag":
        return [["Tczew",53],["Gdansk",63]]
    if state == "Lebork":
        return [["Gdynia",60],["Koscierzyna",58],["Slupsk",55],["Leba",29]]
    if state == "Slupsk":
        return [["Lebork",55],["Bytow",70],["Ustka",21]]
    if state == "Ustka":
        return [["Slupsk",21],["Leba",64]]
    if state == "Leba":
        return [["Ustka",64],["Lebork",29],["Wladyslawowo",66]]
    if state == "Wladyslawowo":
        return [["Leba",66],["Gdynia",42],["Hel",35]]
    if state == "Hel":
        return [["Wladyslawowo",35]]
    return[]

def duplicate_node_path_check(tree, node):

    current_node = node
    

    while  current_node.is_root() == False:
        current_node = tree.parent(current_node.identifier)
        print(current_node)
        if current_node.tag == node.tag :#(i id korzenia)
            print()
            return True, print("true",current_node)
    
    return False,print("false",current_node)

def breadth_first_search(start_state,target_state):
    #do budowy drzewa potrzebujemy dla kazdego wierzcholka id
    #bedziemy je pozniej inkrementowac
    id = 0
    #wrzucenie stanu startowego do drzewa (korzen) i kolejki
    tree = Tree()
    current_node = tree.create_node(start_state,id)#korzen?
    #print("korzen",current_node)
    fifo_queue = []
    fifo_queue.append(current_node)
   
    #petla szukajaca sciezki do stnau koncowego
    #robimy ograniczenie na max wierzcholkow (id<200000)
    while id<200000:
        #jesli kolejka pusta to znaczy ze nie da sie dojsc do stanu koncowego
        #drukowanie kolejki: 
        #print(fifo_queue)
        if len(fifo_queue) == 0:
            #tree.show()
            print("failed to reach the target state")
            return 1
        #jesli kolejka niepusta to wez pierwszy stan z kolejki
        current_node = fifo_queue[0]

        #print("node z kolejki",current_node)
        #jesli ten stan jest koncowy to zakoncz program z sukcesem
        if current_node.tag == target_state:
            #tree.show()
            print("the target state "+str(current_node.tag)+" with id = "+str(current_node.identifier)+" has been reached!")
            return 0
        #jesli stan niekoncowy to usun go z kolejki
        del(fifo_queue[0])
        #a nastepnie dodaj stany osiagalne z niego
        #na koniec kolejki i do drzewa

        print("przed ifem tree i curent node",current_node)
        if   duplicate_node_path_check(tree,current_node) == False: 

            for elem in reachable_states(current_node.tag): 
                
               
                id += 1
                new_elem = tree.create_node(elem[0], id, parent=current_node.identifier)  
                fifo_queue.append(new_elem) 
                

    print("time limit exceeded")
 
 
start = time.time()
breadth_first_search("Gdansk","Ustka")
end = time.time()
print(end - start)
