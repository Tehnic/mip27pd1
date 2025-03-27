goal_number = 300000
start_number = 23

def recursion(tree, current):
    if current.number < goal_number:
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
        self.heuristic = 0
        self.algorithm_value = None
        # self.addedCoef = None


class Tree:
    def __init__(self, number, player, children):
        self.root = Node(number=number, player=player, children=children)

    def insert(self, current, coef):
        if current.number < goal_number:
            new_node = Node(
                number = (current.number * coef),
                player = (current.player * (-1)),
                points = (current.points + 1) if ((current.number * coef)%2 == 0) else (current.points - 1),
                bank = (current.bank + 1) if ((current.number * coef) % 10 in {0,5}) else current.bank,
                children=[],
                # addedCoef = coef
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
            current.children.append(new_node)
            return new_node
        
    def display(self, node=None, indent=0):
        if node is None:
            node = self.root
        # Форматированный вывод текущего узла с отступами:
        print(" " * indent + f"Node(number={node.number}, player={node.player}, points={node.points}, bank={node.bank}, heuristic={node.heuristic})")
        for child in node.children:
            self.display(child, indent + 4)

    def determine_winner(self):
        end_states = []
        
        def find_end_states(node):
            if not node.children:
                end_states.append(node)
            for child in node.children:
                find_end_states(child)
        
        find_end_states(self.root)

        for state in end_states:
            if state.number >= goal_number:
                final_points = state.points
                
                if final_points % 2 == 0:  
                    final_points = final_points - state.bank
                else:  
                    final_points = final_points + state.bank
                
                if final_points % 2 == 0:  
                    print(f"Game ends with number {state.number}, original points {state.points}, bank {state.bank}, final points {final_points}: Player 1 wins")
                else: 
                    print(f"Game ends with number {state.number}, original points {state.points}, bank {state.bank}, final points {final_points}: Player 2 wins") 

# tree.insert(root)

# for node in root.children:
#     tree.insert(node)


