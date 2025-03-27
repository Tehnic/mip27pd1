from koks import Tree, recursion, start_number
from parm_dziluma import depth_limited_search, print_depth_limited_search, limit
from minimaks import minimaks_algorithm
from alfabeta import alfabeta_algorithm
import global_variables
# from heuristic import calculate_heuristic

global_variables.chosenPlayer = int(input("Choose who starts playing: 1-computer, -1-user: "))

tree = Tree(number=start_number, player=global_variables.chosenPlayer, children=[])
root = tree.root

recursion(tree, root)

# tree.display()
# tree.determine_winner()

chosenAlgorithm = int(input("Choose algorithm: 0-minimaks, 1-alphabeta: "))

currentNode = tree.root
while currentNode.number < 300000:
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