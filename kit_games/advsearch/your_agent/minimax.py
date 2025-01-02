import random
from typing import Tuple, Callable


def minimax_move(state, max_depth: int, eval_func: Callable) -> Tuple[int, int]:
    """
    Returns a move computed by the minimax algorithm with alpha-beta pruning for the given game state.
    :param state: state to make the move (instance of GameState)
    :param max_depth: maximum depth of search (-1 = unlimited)
    :param eval_func: the function to evaluate a terminal or leaf state (when search is interrupted at max_depth)
                    This function should take a GameState object and a string identifying the player,
                    and should return a float value representing the utility of the state for the player.
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """
    player = state.player
    value, action = max_value(state, float('-inf'), float('inf'), eval_func, max_depth, 0, player)
    return action


def max_value(state, alpha, beta, eval_func, max_depth, depth, player) -> Tuple[float, Tuple[int, int]]:
    if state.is_terminal() or (max_depth != -1 and depth >= max_depth):
        return eval_func(state, player), None

    value = float('-inf')
    action = None

    for new_action in state.legal_moves():
        sucessor = state.next_state(new_action)
        new_value, x = min_value(sucessor, alpha, beta, eval_func, max_depth, depth + 1, player)
        if new_value > value:
            value = new_value
            action = new_action
        alpha = max(alpha, value)
        if alpha >= beta:
            break

    return value, action


def min_value(state, alpha, beta, eval_func, max_depth, depth, player) -> Tuple[float, Tuple[int, int]]:
    if state.is_terminal() or (max_depth != -1 and depth >= max_depth):
        return eval_func(state, player), None

    value = float('inf')
    action = None

    for new_action in state.legal_moves():
        sucessor = state.next_state(new_action)
        new_value, x = max_value(sucessor, alpha, beta, eval_func, max_depth, depth + 1, player)
        if new_value < value:
            value = new_value
            action = new_action
        beta = min(beta, value)
        if beta <= alpha:
            break

    return value, action
