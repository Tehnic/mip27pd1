import global_variables


def calculate_heuristic(points, bank):
    parity_factor = 0

    if global_variables.chosen_player == 1:
        if (points % 2 == 0 and bank % 2 == 0) or (points % 2 != 0 and bank % 2 != 0):
            parity_factor = 1
        else:
            parity_factor = -1
    else:
        if (points % 2 == 0 and bank % 2 == 0) or (points % 2 != 0 and bank % 2 != 0):
            parity_factor = -1
        else:
            parity_factor = 1

    return parity_factor
