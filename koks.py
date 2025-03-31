import global_variables
goal_number = global_variables.limit


def recursion(tree, current):
    if current.number < goal_number:
        new_node = tree.insert(current, coef=3)
        recursion(tree=tree, current=new_node)
        new_node = tree.insert(current, coef=4)
        recursion(tree=tree, current=new_node)
        new_node = tree.insert(current, coef=5)
        recursion(tree=tree, current=new_node)


class Node:
    def __init__(self, number, player, children, points=0, bank=0):
        # Stāvokļa parametri
        self.number = number
        self.points = points
        self.bank = bank
        # Darbības parametri
        self.player = player
        self.children = children
        self.heuristic = 0
        self.algorithm_value = None


class Tree:
    def __init__(self, number, player, children):
        self.root = Node(number=number, player=player, children=children)

    def insert(self, current, coef):
        if current.number < goal_number:
            new_node = Node(
                number=(current.number * coef),
                player=(current.player * (-1)),
                points=(current.points + 1) if ((current.number * coef) % 2 == 0) else (current.points - 1),
                bank=(current.bank + 1) if ((current.number * coef) % 10 in {0, 5}) else current.bank,
                children=[],
            )
            current.children.append(new_node)
            return new_node
