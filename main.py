from koks import Tree, recursion, start_number
from parm_dziluma import depth_limited_search, print_depth_limited_search, limit
from heuristic import calculate_heuristic

tree = Tree(number=start_number, player=1, children=[])
root = tree.root

recursion(tree, root)

tree.display()
tree.determine_winner()

dfs_results = depth_limited_search(tree.root, limit)

print("\n🔍 DFS Результаты с эвристикой:")
print("=" * 50)
for node, coef in dfs_results:
    heuristic_value = calculate_heuristic(node.number, node.points, node.bank)
    print(f"Number: {node.number}, Player: {node.player}, Points: {node.points}, Bank: {node.bank}, "
          f"Multiplier: {coef}, Heuristic: {heuristic_value}")
    print("-" * 50)

print_depth_limited_search(dfs_results)      