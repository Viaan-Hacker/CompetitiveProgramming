"""
Program that uses cannonical strings to solve the rooted tree isomporphism
problem under the reshuffling rule.

--> The root node always remains in this position, i.e., as root.
--> Each other node remains connected to its original parent node.
--> Each node (root or not) branches out to the same set of nodes but the order of outgoing branches
    may change in an arbitrary way.

Input is taken from a text file.
Output is written to a text file.

Input example (in text file):
4
7 -1 0 0 6 6 6 0
7 -1 0 1 1 6 6 1
7 -1 3 3 0 3 0 0
7 -1 3 3 0 5 0 0
0

The first line indictes the number of trees, N. 
The last line indicates the end of input.
Each line line between N and the end of input reprsents a tree.
The first line of that line indicates the number of nodes in that tree.
Nodes are labeled, [0, 1, ..., 5, 6].
Root nodes are labeled -1. 
i.e in the line 7 -1 0 0 6 6 6 0, we have that there are 7 nodes.
Now the nodes, [0, 1, 2, 3, 4, 5, 6] have the following connections,
[-1 0 0 6 6 6 0].

We have that node 0 is the root node.
Nodes, 1, 2 and 6 are children of node 0.
Nodes, 3, 4 and 5 are children of 6.


A sample output for the above input would be:
0: 0 1 0 2

This is because the first and third trees are equivalent under rooted tree isomorphism
under the reshuffling rule. So they recieve the same class, 0.
Trees 2 and 4 are distinict from all other trees in this input so they each get their own class, 1 and 2. 
"""


import sys

class Tree:
    def __init__(self, root):
        self.data = dict()
        self.root = root
        self.cannonical_string = None

    def add_edge(self, node1, node2):
        if node1 in self.data:
            self.data[node1].append(node2)
        else:
            self.data[node1] = [node2]

        if node2 in self.data:
            self.data[node2].append(node1)
        else:
            self.data[node2] = [node1]

    def get_canonical_string(self, current_node, parent_node):
        children = []
        for child_node in self.data[current_node]:
            if child_node == parent_node:
                continue
            else:
                pass
            
            children.append(self.get_canonical_string(child_node, current_node))   

        children.sort()
        canonical_string = "("     
        for child in children:
            canonical_string += child
        canonical_string += ")"
        return canonical_string


    def __str__(self):
        return str(self.data)

def get_root_tuple(tree_string):
    return (tree_string.index("-1") - 1, "-1")

def get_input_std():
    data_dictionary = {}


    data = [x.split() for x in sys.stdin.readlines()]

    scenario_number = 0    
    while data[0][0] != "0":
        trees_as_string_lists = data[1:int(data[0][0]) + 1]
        
        for tree in trees_as_string_lists:
            edge_list = [(x, int(tree[x + 1])) for x in range(int(tree[0]))]
            root = get_root_tuple(tree)
            T = Tree(root)
            for edge in edge_list:
                T.add_edge(edge[0], edge[1])

            T.cannonical_string = T.get_canonical_string(T.root[0], T.root[1])

            if scenario_number in data_dictionary:                
                data_dictionary[scenario_number].append(T)
            else:
                 data_dictionary[scenario_number] = [T]

        scenario_number += 1               
        data = data[int(data[0][0]) + 1:]

    return data_dictionary

def main():
    data_dictionary = get_input_std()
    
    final_output_string = ""
    for scenario_number, trees in data_dictionary.items():
        scenario_number_output_string = str(scenario_number) + ": "

        unique_string_mapping_dict = {string: None for string in set([T.cannonical_string for T in trees])}

        next_class_number = 1
        if len(trees) > 0:
            unique_string_mapping_dict[trees[0].cannonical_string] = 0

            for T in trees:
                if  unique_string_mapping_dict[T.cannonical_string] == None:
                    unique_string_mapping_dict[T.cannonical_string] = next_class_number
                    next_class_number += 1

                scenario_number_output_string = scenario_number_output_string + str(unique_string_mapping_dict[T.cannonical_string]) + " "


            final_output_string = final_output_string + scenario_number_output_string + "\n"

        else:
            final_output_string = final_output_string + scenario_number_output_string + "\n"

    new = final_output_string.strip()
    print(new)
  

main()

