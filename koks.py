def recursion(tree, current):
    if current.number < 3000:
        newNode = tree.insert(current, coef = 3)
        recursion(tree = tree, current = newNode)
        newNode = tree.insert(current, coef = 4)
        recursion(tree = tree, current = newNode)
        newNode = tree.insert(current, coef = 5)
        recursion(tree = tree, current = newNode)

class Node:

    def __init__(self, number, player, children,  points = 0, bank=0):
        # Stāvokļa parametri
        self.number = number
        self.points = points
        self.bank = bank
        # Darbības parametri
        self.player = player
        self.children = children


class Tree:

    def __init__(self, number, player, children):
        self.root = Node(number=number, player=player, children=children)

    def insert(self, current, coef):
        if current.number < 3000:
            node1 = Node(
                number = (current.number * coef),
                player = (current.player * (-1)),
                points = (current.points + 1) if ((current.number * coef)%2 == 0) else (current.points - 1),
                bank = (current.bank + 1) if ((current.number * coef) % 10 in {0,5}) else current.bank,
                children=[]
            )
            # node2 = Node(
            #     number = (current.number * 4), 
            #     player = (current.player * (-1)), 
            #     points = (current.points + 1) if ((current.number * 4)%2 == 0) else (current.points - 1), 
            #     bank = (current.bank + 1) if ((current.number * 4) % 10 in {0,5}) else current.bank
            # )
            # node3 = Node(
            #     number = (current.number * 5),
            #     player = (current.player * (-1)),
            #     points = (current.points + 1) if ((current.number * 5)%2 == 0) else (current.points - 1),
            #     bank = (current.bank + 1) if ((current.number * 5) % 10 in {0,5}) else current.bank
            # )
            current.children.append(node1)
            return node1

tree = Tree(number=20, player=1, children=[])
root = tree.root
# tree.insert(root)

# for node in root.children:
#     tree.insert(node)

recursion(tree, root)


