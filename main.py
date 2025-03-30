from koks import Tree, recursion, start_number
from parm_dziluma import depth_limited_search, print_depth_limited_search, limit
from minimaks import minimaks_algorithm
from alfabeta import alfabeta_algorithm
import global_variables
# from heuristic import calculate_heuristic

global currentNode
global choosenAlgorithm


def choose_player(ui_input=None):
    if ui_input is None:
        global_variables.chosenPlayer = int(input("Choose who starts playing: 1-computer, -1-user: "))
    else:
        global_variables.chosenPlayer = ui_input

def generate_tree(ui_input=None):
    if ui_input is None:        
        #tree = Tree(number=start_number, player=global_variables.chosenPlayer, children=[])
        main_start_number=0
        while main_start_number<20 or 30<main_start_number:
            main_start_number=int(input("INPUT A NUMBER FROM 20 TO 30: "))
        tree = Tree(number=main_start_number, player=global_variables.chosenPlayer, children=[])
    else:
        tree = Tree(number=ui_input, player=global_variables.chosenPlayer, children=[])
    #global root 
    root = tree.root

    recursion(tree, root)
    
    #tree.display()
    #tree.determine_winner()
    return tree

#global chosenAlgorithm
#chosenAlgorithm-=0
#global currentNode
def choose_algorithm(ui_input=None):
    #global chosenAlgorithm
    if ui_input is None:
        chosenAlgorithm = int(input("Choose algorithm: 0-minimaks, 1-alphabeta: "))
    else:
        chosenAlgorithm = ui_input
    #global currentNode
    #currentNode = tree.root
    return chosenAlgorithm
    
def computer_logic(chosen_algorithm, ui_input=None, ui_limit=None):
    if ui_input is None:
        tree = Tree(number=23, player=global_variables.chosenPlayer, children=[])
    else:
        tree = ui_input
    other_limit=2    
    if ui_limit is None:
        other_limit=3000
    else:
        other_limit=ui_limit
    root = tree.root
    recursion(tree, root)
    currentNode=tree.root
    
    chosenAlgorithm=1
    chosenAlgorithm=chosen_algorithm
    #print("chosenPlayer",global_variables.chosenPlayer," algorithm",chosenAlgorithm)
    #while currentNode.number < 300000:
    i=0
    while currentNode.number < 300000 and i<other_limit:
        i=i+1
        print(f"number= {currentNode.number} bank= {currentNode.bank} points= {currentNode.points} her= {currentNode.heuristic} alg_val= {currentNode.algorithm_value}")
        if currentNode.player == 1:
            if all(child.algorithm_value is None for child in currentNode.children):
                dfs_results = depth_limited_search(currentNode, limit)
                if(chosenAlgorithm == 0):
                    minimaks_algorithm(currentNode, limit)
                else:
                    alfabeta_algorithm(currentNode, limit)
            currentNode = next(
                (child for child in currentNode.children if child.algorithm_value == currentNode.algorithm_value),
                None
            )
        else:
            userCoef = int(input("Enter your coef: "))
            currentNode = next(
                (child for child in currentNode.children if child.number == currentNode.number * userCoef),
                None
            )
        
        if(other_limit==1):
            return currentNode.number
        

    print(f"number= {currentNode.number} bank= {currentNode.bank} points= {currentNode.points} her= {currentNode.heuristic} alg_val= {currentNode.algorithm_value}")
    

# tree.display()
# print("\n🔍 DFS Результаты с эвристикой:")
# print("=" * 50)
# for node, coef in dfs_results:
#     # heuristic_value = calculate_heuristic(node.number, node.points, node.bank)
#     print(f"Number: {node.number}, Player: {node.player}, Points: {node.points}, Bank: {node.bank}, "
#           f"Multiplier: {coef}, Heuristic: {node.heuristic}")
#     print("-" * 50)

# print_depth_limited_search(dfs_results)



if __name__ == "__main__":
    choose_player()
    main__chosen_algorithm=choose_algorithm()
    main_tree=generate_tree()
    computer_logic(main__chosen_algorithm, main_tree)      