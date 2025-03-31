import global_variables
limit = 3
def alfabeta_algorithm(node, limit, alpha=float('-inf'), beta=float('inf'), depth=0): 
    global_variables.visitedNodes += 1
    if depth > limit:
        return []
    elif depth == limit or not node.children:
        node.algorithm_value = node.heuristic
        return node.algorithm_value

    if node.player == 1:  
        max_eval = float('-inf')
        for child in node.children:
            eval_value = alfabeta_algorithm(child, limit, alpha, beta, depth + 1)
            max_eval = max(max_eval, eval_value)
            alpha = max(alpha, eval_value)
            if beta <= alpha:  
                break
        node.algorithm_value = max_eval
        return max_eval
    else: 
        min_eval = float('inf')
        for child in node.children:
            eval_value = alfabeta_algorithm(child, limit, alpha, beta, depth + 1)
            min_eval = min(min_eval, eval_value)
            beta = min(beta, eval_value)
            if beta <= alpha:
                break
        node.algorithm_value = min_eval
        return min_eval
