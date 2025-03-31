from koks import Tree, recursion
from minimaks import minimaks_algorithm
from alfabeta import alfabeta_algorithm
import global_variables
import MIP_front
import logging
import time


def choose_player(ui_input=None):
    global_variables.chosenPlayer = ui_input
    chosen_player = ui_input
    return chosen_player


def generate_tree(ui_input=None):
    tree = Tree(number=ui_input, player=global_variables.chosen_player, children=[])
    root = tree.root
    recursion(tree, root)
    return tree


def choose_algorithm(ui_input=None):
    chosen_algorithm = ui_input
    return chosen_algorithm


def computer_logic(chosen_algorithm, ui_input=None):
    tree = ui_input
    root = tree.root
    recursion(tree, root)
    current_node = tree.root

    logging.basicConfig(filename="game.log", level=logging.INFO, datefmt="%H:%M:%S.%f")

    if current_node.number < global_variables.limit:
        if current_node.player == 1:
            global_variables.visitedNodes = 0
            start = time.perf_counter()
            if all(child.algorithm_value is None for child in current_node.children):
                if chosen_algorithm == 0:
                    minimaks_algorithm(current_node, global_variables.max_depth)
                else:
                    alfabeta_algorithm(current_node, global_variables.max_depth)
            current_node = next(
                (child for child in current_node.children if child.algorithm_value == current_node.algorithm_value),
                None)
            end = time.perf_counter()
            logging.info(f"Gajiena laiks {(end - start)*1000:.3f} ms, Apmekletas virsotnes {global_variables.visited_nodes}")
            global_variables.visited_nodes = 0

    return current_node.number


if __name__ == "__main__":
    MIP_front.start_game() 
