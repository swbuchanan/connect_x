from abc import abstractmethod
from board import Board
import random

class Player:
    def __init__(self, id, color):
        self.id = id
        self.color = color

    @abstractmethod
    def make_move(self, board) -> int:
        """Given a board state, return the index of the column where we want to drop a piece"""
        ...

class HumanPlayer(Player):
    def get_move(self, board: Board):
        return None

class RandomPlayer(Player):

    def get_move(self, board: Board):
        """Play a random move"""
        valid_locs = [board.is_valid_location(col) for col in range(board.width)]
        return random.choice(valid_locs)