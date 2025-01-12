tree = [
    "root", [
        "child1", [
            ["child1.1", []],
            ["child1.2", []]
        ]
    ],
    ["child2", []]
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
add_child("child1.3", tree[1][1])
add_sibling("child2.1", tree[2])
add_sibling("child2.2", tree[2])

add_child("child3", tree)
add_sibling("child3.1", tree[3])
edit_node("root1", tree)

print_tree(tree)
print("===============")
delete_node(tree[1])
print_tree(tree)
