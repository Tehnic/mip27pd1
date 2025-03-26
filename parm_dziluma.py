from heuristic import calculate_heuristic

limit = 3
# Поиск в глубину с ограничением
def depth_limited_search(node, limit, depth=0, coef=1):
    if depth > limit:
        return []
    
    result = [(node, coef)] 
    node.heuristic = calculate_heuristic(node.number, node.points, node.bank)
    
    for child in node.children:
        child_results = depth_limited_search(child, limit, depth + 1, coef=child.number // node.number)
        result.extend(child_results)
    
    return result

def print_depth_limited_search(dfs_res):
    print(f"DFS result with limit {limit}:")
    print("=" * 50)
    for node, coef in dfs_res:
        print(f"Number: {node.number}, Player: {node.player}, Points: {node.points}, Bank: {node.bank}, Multiplier: {coef}")
        print("-" * 50)

