from typing import Tuple
from ..othello.gamestate import GameState
from ..othello.board import Board
from .minimax import minimax_move


def make_move(state: GameState) -> Tuple[int, int]:
    """
    Returns a move for the given game state
    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """

    # A chamada a minimax_move deve receber sua funcao evaluate como parametro.
    return minimax_move(state, max_depth=5, eval_func=evaluate_count)


def evaluate_count(state: GameState, player: str) -> float:
    """
    Evaluates an othello state from the point of view of the given player.
    If the state is terminal, returns its utility.
    If non-terminal, returns an estimate of its value based on the number of pieces of each color.
    :param state: state to evaluate (instance of GameState)
    :param player: player to evaluate the state for (B or W)
    """
    if state.is_terminal():
        winner = state.winner()
        if winner == player:
            return 1.0
        elif winner is None:
            return 0.0
        else:
            return -1.0

    board = state.board.tiles
    player_count = sum(row.count(player) for row in board)
    opponent_count = sum(row.count("B" if player == "W" else "W") for row in board)
    return player_count - opponent_count
