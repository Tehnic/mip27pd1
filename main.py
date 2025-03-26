from koks import Tree, recursion, start_number
from parm_dziluma import depth_limited_search, print_depth_limited_search, limit
from minimaks import minimaks_algorithm
# from heuristic import calculate_heuristic

tree = Tree(number=start_number, player=1, children=[])
root = tree.root

recursion(tree, root)

# tree.display()
# tree.determine_winner()

currentNode = tree.root
while currentNode.number < 3000:
    print(currentNode.number)
    if currentNode.player == 1:
        if all(child.algorithm_value is None for child in currentNode.children):
            dfs_results = depth_limited_search(currentNode, limit)
            minimaks_algorithm(currentNode, limit)
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

print(currentNode.number)

# tree.display()
# print("\n🔍 DFS Результаты с эвристикой:")
# print("=" * 50)
# for node, coef in dfs_results:
#     # heuristic_value = calculate_heuristic(node.number, node.points, node.bank)
#     print(f"Number: {node.number}, Player: {node.player}, Points: {node.points}, Bank: {node.bank}, "
#           f"Multiplier: {coef}, Heuristic: {node.heuristic}")
#     print("-" * 50)

# print_depth_limited_search(dfs_results)      