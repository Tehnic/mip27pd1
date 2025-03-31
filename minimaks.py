import global_variables

limit = 3
def minimaks_algorithm(node, limit, depth=0):
    global_variables.visitedNodes += 1
    if depth > limit:
        return []
    elif depth == limit or not node.children:
        node.algorithm_value = node.heuristic
        return
    for child in node.children:
        if child.algorithm_value is None:
            minimaks_algorithm(child, limit, depth+1) 
        if node.player == 1:
            if node.algorithm_value is None or node.algorithm_value < child.algorithm_value:
                node.algorithm_value = child.algorithm_value
        else:
            if node.algorithm_value is None or node.algorithm_value > child.algorithm_value:
                node.algorithm_value = child.algorithm_value
