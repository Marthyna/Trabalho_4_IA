from typing import Tuple
from ..othello.gamestate import GameState
from ..othello.board import Board
from .minimax import minimax_move

# mask template adjusted from https://web.fe.up.pt/~eol/IA/MIA0203/trabalhos/Damas_Othelo/Docs/Eval.html
# could optimize for symmetries but just put all values here for coding speed :P
# DO NOT CHANGE!
EVAL_TEMPLATE = [
    [100, -30, 6, 2, 2, 6, -30, 100],
    [-30, -50, 1, 1, 1, 1, -50, -30],
    [6, 1, 1, 1, 1, 1, 1, 6],
    [2, 1, 1, 3, 3, 1, 1, 2],
    [2, 1, 1, 3, 3, 1, 1, 2],
    [6, 1, 1, 1, 1, 1, 1, 6],
    [-30, -50, 1, 1, 1, 1, -50, -30],
    [100, -30, 6, 2, 2, 6, -30, 100],
]


def make_move(state: GameState) -> Tuple[int, int]:
    """
    Returns a move for the given game state
    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """

    # A chamada a minimax_move deve receber sua funcao evaluate como parametro.
    return minimax_move(state, max_depth=5, eval_func=evaluate_mask)


def evaluate_mask(state: GameState, player: str) -> float:
    """
    Evaluates an othello state from the point of view of the given player.
    If the state is terminal, returns its utility.
    If non-terminal, returns an estimate of its value based on the positional value of the pieces.
    You must use the EVAL_TEMPLATE above to compute the positional value of the pieces.
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

    opponent = Board.opponent(player)
    player_score = 0
    opponent_score = 0

    for y in range(8):
        for x in range(8):
            square_color = state.board.tiles[y][x]
            if square_color == player:
                player_score += EVAL_TEMPLATE[y][x]
            elif square_color == opponent:
                opponent_score += EVAL_TEMPLATE[y][x]

    return player_score - opponent_score
