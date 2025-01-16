tree = [
    "root", [ #tree[0]
        "child1", [  # tree[1][0]
                    ["child1.1",  # tree[1][1]
                        [] # tree[1][1][0]
                    ], 
                   ["child1.2", # tree[1][2] 
                        []  # tree[1][2][0]
                    ]
                   ],
        "child2", [ # tree[1][3]
                    ["child2.1", # tree[1][4]
                        [] # tree[1][4][0]
                    ]
                ],
        "child3", []
    ], 

]


def print_tree(tree, level=0):
    for node in tree:
        if type(node) == list:
            print_tree(node, level + 1)
        else:
            print(" " * level, node)


def add_child(value, parent):
    parent.append([value, []])


def add_sibling(value, parent):
    parent[-1].append([value, []])


def edit_node(value, parent):
    parent[-1][0] = value


def delete_node(parent):
    parent.pop()
    
print_tree(tree)
print("===============")
# add child in child1
add_child("child1.3", tree[1][1])
print_tree(tree)
print("===============")
# add child in child3

add_child("child3.1", tree[1][5])
print_tree(tree)