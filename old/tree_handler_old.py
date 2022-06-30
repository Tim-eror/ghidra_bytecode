class Node:
    def __init__(self, data):
        self.childs = []
        self.data = data

    



def main():
    root = Node("hallo")
    root.childs.append("bard")  
    root.childs.append("welt")     
    insert_note("hallobarden",root)

# Determines the number of differnet chars between a and b
def calc_diff_num(a,b):
    count = 0
    for i in range(min(len(a),len(b))):
        if a[i] is not b[i] or a[i] is "*":
            return count
        else:
            count += 1

    return count 



def insert_note(code_str, current_node: Node): 
    
    c = calc_diff_num(current_node.data, code_str) # c is the number of matching characters 
    len_c = len(current_node.data)
    if c == 0: # if there is no matching.... well i think i have a problem
        print("OOPS: No match at all")
        return

    elif c < len_c: #if the word partly matches we need to split the current node and add the two parts as children
        current_node_str = current_node.data
        current_node.data = current_node_str[:c]
        current_node.childs.append(current_node_str[c:])
        current_node.childs.append(code_str[c:])

    elif c == len_c: #if the word fully matches the node data we can look at the children and use the only matching one
        for child in current_node.childs:
            if child.data.startswith(code_str[0]):
                insert_note(code_str[c:], child)
                return
        #only reacheble if non of the childs matches.
        current_node.childs.append(Node(code_str[c:])) # create new node


    





if __name__ == "__main__":
    main()





            




